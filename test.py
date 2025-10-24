from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
import json

# elements = partition("layout-parser-paper-with-table.pdf")
# elements = partition("layout-parser-paper.pdf")
# print("\n\n".join([str(el) for el in elements]))

# elements = partition_pdf(
#     filename="humvee_sub_resize.pdf",
#     strategy="hi_res",
#     extract_images_in_pdf=True,
#     extract_image_block_types=["Table"],
#     extract_image_block_to_payload=True,
#     infer_table_structure=True,
#     # extract_image_block_output_dir="nh_humvee",
#     # extract_image_block_crop_horizontal_pad=0,
#     # extract_image_block_crop_vertical_pad=0,
# )

elements = partition_pdf(
                filename="/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/pdfs/data-5-10-20.pdf",
                strategy="hi_res",
                skip_infer_table_types=False,
                # extract_image_block_output_dir=f"{self.result_dir}/tables",
                infer_table_structure=True
            )

# elements = partition_pdf(
#                 filename="humvee_sub_resize.pdf",
#                 strategy="hi_res",
#                 skip_infer_table_types=False,
#                 # extract_image_block_output_dir=f"{self.result_dir}/tables",
#                 infer_table_structure=True,
                
#             )
# tables_data  = [el.to_dict() for el in elements if el.category == "Table"]

# Convert elements to JSON
elements_json = [el.to_dict() for el in elements]
print(elements[0].text)
print(elements[0].metadata.text_as_html)
# # Save JSON metadata
with open("pdf_metadata.json", "w") as f:
    json.dump(elements_json, f, indent=4)

print("JSON metadata saved to pdf_metadata.json")
