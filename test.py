from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
import json

# elements = partition("layout-parser-paper-with-table.pdf")
# elements = partition("layout-parser-paper.pdf")
# print("\n\n".join([str(el) for el in elements]))

elements = partition_pdf(
    filename="humvee_sub_resize.pdf",
    strategy="hi_res",
    extract_images_in_pdf=True,
    extract_image_block_types=["Image", "Table"],
    extract_image_block_to_payload=False,
    extract_image_block_output_dir="humvee_sub_images_resized",
    # extract_image_block_crop_horizontal_pad=0,
    # extract_image_block_crop_vertical_pad=0,
)

# Convert elements to JSON
# elements_json = [el.to_dict() for el in elements]

# # Save JSON metadata
# with open("pdf_metadata.json", "w") as f:
#     json.dump(elements_json, f, indent=4)

# print("JSON metadata saved to pdf_metadata.json")
