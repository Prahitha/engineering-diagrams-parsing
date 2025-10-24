from unstructuredio import UnstructuredPdf, TableImages


# get images, table info from  pdf 
# data = UnstructuredPdf('data/pdfs/data-2.pdf')
# data.extract_figures()
# data.extract_tables()

# get png images of table 
# tables = TableImages('/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/tables_data.json', '/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/pdfs/data-4.pdf', '/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4')
# tables._get_tables()

tables = TableImages('/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/tables_data.json', '')
tables._merge_image_caption_table('/home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/tables_data.json')

# sbt "runMain org.allenai.pdffigures2.FigureExtractorBatchCli /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/pdfs/data-5.pdf -s /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/images.json -m /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/"
# sbt -J-Xmx64G "runMain org.allenai.pdffigures2.FigureExtractorBatchCli /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/pdfs/data-5-1-100.pdf -s /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/images.json -m /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/result_data/data-5/images/"
# sbt -J-Xmx64G "runMain org.allenai.pdffigures2.FigureExtractorBatchCli /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/pdfs/data-4-1-100.pdf -s /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/images.json -m /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/images/"
# python -m olmocr.pipeline /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/table_data/ --markdown --pdfs /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-4/tables/
# chandra /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/tables /home/nagaharshitamarupaka/engineering-diagrams-parsing/ExtractImages/data/results/data-5/table_data --method vllm
