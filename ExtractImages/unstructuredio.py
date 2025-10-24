from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
import json, os
from pdf2image import convert_from_path
import ijson


class UnstructuredPdf:
    def __init__(self, filename):
        self.filename = filename 
        self.result_dir = '/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/'

    def extract_metadata(self):
        elements = partition_pdf(
            filename=self.filename,
            strategy="hi_res",
            extract_images_in_pdf=True,
            extract_image_block_types=["Table"],
            extract_image_block_to_payload=True,
        )

        metadata_json = [el.to_dict() for el in elements]

        with open(f"{self.result_dir}/images_tables_metadata.json", "w") as f:
            json.dump(metadata_json, f, indent=4)

    def extract_figures(self):
        try:
            elements = partition_pdf(
                filename=self.filename,
                strategy="hi_res",
                extract_images_in_pdf=True,
                extract_image_block_types=["Image"],
                extract_image_block_to_payload=False, 
                extract_image_block_output_dir=f"{self.result_dir}/figures",
            )
        except Exception as e:
            print(e)
    
    def extract_tables(self):
        try:
            elements = partition_pdf(
                filename=self.filename,
                strategy="hi_res",
                skip_infer_table_types=False,
                # extract_image_block_output_dir=f"{self.result_dir}/tables",
                infer_table_structure=True,
            )
            tables_data  = [el.to_dict() for el in elements]

            with open(f"{self.result_dir}/tables_data.json", "w") as f:
                json.dump(tables_data, f, indent=4)

        except Exception as e:
            print(e)



class TableImages:
    def __init__(self, json_file, pdf_file):
        self.json_file = json_file
        self.pdf_file = pdf_file
    
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"File not found: {json_file}")

        if os.path.getsize(json_file) == 0:
            raise ValueError(f"File is empty: {json_file}")

        # os.makedirs(self.result_dir, exist_ok=True)

    def _get_tables(self, result_dir):
        """
        Stream through the large JSON file and process pages that contain tables.
        """
        self.result_dir = f'{result_dir}/tables'
        table_pages = set()
        count = 0

        with open(self.json_file, "r", encoding="utf-8") as f:
            # 👇 iterate through each element in the top-level array
            for element in ijson.items(f, "item"):
                count += 1
                # Debug logging (optional)
                if count % 10 == 0:
                    print(f"Processed {count} JSON objects...")

                if element.get("type") == "Table":
                    metadata = element.get("metadata", {})
                    page_number = metadata.get("page_number")
                    if page_number:
                        table_pages.add(page_number)

        print(f"Total Table Pages Found: {len(table_pages)}")

        for page in sorted(table_pages):
            images = convert_from_path(
                self.pdf_file,
                first_page=page,
                last_page=page
            )
            if images:
                save_path = f"{self.result_dir}/page_{page}.png"
                images[0].save(save_path, "PNG")
                print(f"Saved: {save_path}")


    def _merge_image_caption_table(self, json_file_path):
        """
        Merges Images, Tables, and FigureCaptions from a JSON file.
        Returns the merged images dict and also saves it to a JSON file in the same directory.
        """
        try:
            # Directory containing the JSON file
            file_dir = os.path.dirname(json_file_path)
            os.makedirs(file_dir, exist_ok=True)  # ensure directory exists

            images = {}

            # Stream JSON file for memory efficiency
            with open(json_file_path, "r") as f:
                elements = ijson.items(f, "item")  # assumes top-level list
                for element in elements:
                    metadata = element.get("metadata", {})
                    page_number = metadata.get("page_number")
                    if page_number is None:
                        continue

                    elem_type = element.get("type")

                    # Image
                    if elem_type == "Image":
                        images[page_number] = element

                    # Table
                    elif elem_type == "Table":
                        prev_page = page_number - 1
                        if prev_page in images:
                            images[prev_page]["table"] = element
                            images[prev_page]["table_image"] = os.path.join(file_dir, "tables", f"page-{page_number}")
                            images[prev_page]["table_data"] = os.path.join(file_dir, "table_data", f"page-{page_number}")

                    # FigureCaption
                    elif elem_type == "FigureCaption":
                        if page_number in images:
                            images[page_number]["caption"] = element
                            text = element.get("text", "")
                            idx = 8 if len(text) > 8 else 0
                            images[page_number]['image_path'] = os.path.join(file_dir, "images", f"Figure-{text[idx]}.png")

            filtered_images = {
                k: v for k, v in images.items()
                if "table" in v and "caption" in v
            }
            print(len(filtered_images))

            # Save merged images dict to a JSON file
            output_json_path = os.path.join(file_dir, "merged_data.json")
            with open(output_json_path, "w") as out_f:
                json.dump(filtered_images, out_f, indent=2, default=float)

            return images

        except Exception as e:
            print(f"Error processing JSON file {json_file_path}: {e}")
            return {}


"""
image number - 


"""