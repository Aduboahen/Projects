# !python3

# convert html to pdf

import pdfcrowd, os, requests, time


try:
    os.makedirs('./output', exist_ok=True)
    out_path = os.path.join(os.getcwd(), './output')
    link = str(input('Enter the link (You can copy and paste): \n'))
    requests.get(link).raise_for_status()
    pdf_file = str(input('Enter name for the pdf file: \n')) + '.pdf'


    api = pdfcrowd.HtmlToPdfClient("demo", "ce544b6ea52a5621fb9d55f8b542d14d")
    api.convertUrlToFile(link, os.path.join(out_path, pdf_file))

    print('Converting webpage to pdf. PDF file will be saved to the "Output" folder in the extracted folder')

except HTTPError as e:
    raise Exception(f'Invalid url {}')
    print('Please enter a valid url.')

time.sleep(5)
