# PDF Indexor

This script will allow indexing of a PDF file, extracting portion of the PDF file and export it to the specified path as a separate PDF file.

### Dependencies

- _pyPDF2_

```
pip install pypdf2
```

### Running the script

**_Starting and ending page number must exactly match the page number as displayed in pdf readers, not the actual page number_**<br>
Clone the script and run following command in terminal: <br>

```
python index_pdf.py <path_to_file/filename.pdf> <export_path.pdf> <starting_index> <ending_index>
```
