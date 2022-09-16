{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5e8b5991",
   "metadata": {},
   "source": [
    "## Notebook to convert popular different Image file types into PDF and Vice-Versa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "99bfbf48",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing Dependencies\n",
    "\n",
    "from PIL import Image\n",
    "from pdf2image import convert_from_path\n",
    "from PyPDF2 import PdfFileMerger\n",
    "import os"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "304a18bc",
   "metadata": {},
   "source": [
    "#### PDF to JPG"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "ab6afc74",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Image_Convertor:\n",
    "    \n",
    "    def pdf_2_jpg():\n",
    "        # Setting the I/P & O/P file paths\n",
    "        IP_path = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/\" \n",
    "\n",
    "        OP_path1 = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/Jpeg/\" #jpg path\n",
    "\n",
    "        pdfname = IP_path + input('Enter PDF name with extension: ')\n",
    "\n",
    "        # Counting the number of pages in the pdf and converting the pages into image\n",
    "        images = convert_from_path(pdfname)\n",
    "        i = 1\n",
    "        length = len(images)\n",
    "\n",
    "        print(\"Number of pages in PDF=\"+str(length))\n",
    "\n",
    "        for image in images:\n",
    "            image.save(OP_path1 + str(i) + '.jpg', 'JPEG')\n",
    "            i = i + 1\n",
    "        \n",
    "    def pdf_2_png():\n",
    "        # Setting the I/P & O/P file paths\n",
    "        IP_path = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/\" \n",
    "\n",
    "        OP_path2 = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/png/\" #png path\n",
    "\n",
    "        pdfname = IP_path + input('Enter PDF name with extension: ')\n",
    "\n",
    "        # Counting the number of pages in the pdf and converting the pages into image\n",
    "        images = convert_from_path(pdfname)\n",
    "        i = 1\n",
    "        length = len(images)\n",
    "\n",
    "        print(\"Number of pages in PDF=\"+str(length))\n",
    "\n",
    "        for image in images:\n",
    "            image.save(OP_path2 + str(i) + '.png', 'PNG')\n",
    "            i = i + 1\n",
    "    \n",
    "    def png_2_pdf():\n",
    "        \n",
    "        IP_path2 = r\"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/png/\"\n",
    "        OP_path = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/PDF/\"\n",
    "        \n",
    "        #\n",
    "        \n",
    "        img_list = [os.path.join(IP_path2, file)\n",
    "                for file in os.listdir(IP_path2)\n",
    "                if file.endswith('.png')]\n",
    "\n",
    "        for i,path in enumerate(img_list):\n",
    "            image_1 = Image.open(path)\n",
    "            im_1 = image_1.convert('RGB')\n",
    "            im_1.save(OP_path+str(i)+'.pdf')    \n",
    "        \n",
    "    def jpg_2_pdf():\n",
    "        IP_path1 = r\"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/Jpeg/\"\n",
    "        OP_path = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/PDF/\"\n",
    "\n",
    "        img_list = [os.path.join(IP_path1, file)\n",
    "                for file in os.listdir(IP_path1)\n",
    "                if file.endswith('.jpg')]\n",
    "\n",
    "        for i,path in enumerate(img_list):\n",
    "            new_image_1 = Image.open(path)\n",
    "            new_im_1 = new_image_1.convert('RGB')\n",
    "            new_im_1.save(OP_path+str(i)+'.pdf')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "6e73cc77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter PDF name with extension: sample.pdf\n",
      "Number of pages in PDF=32\n"
     ]
    }
   ],
   "source": [
    "Image_Convertor.pdf_2_jpg()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fe3f7b61",
   "metadata": {},
   "outputs": [],
   "source": [
    "Image_Convertor.jpg_2_pdf()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83f8b1d9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb99d8dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# fuction to merge all pdfs into a single pdf in a given folder\n",
    "def merge_pdf():\n",
    "\n",
    "    pdf_list = [os.path.join(OP_path, file)\n",
    "            for file in os.listdir(OP_path)\n",
    "            if file.endswith('.pdf')]\n",
    "\n",
    "    merger = PdfFileMerger()\n",
    "\n",
    "    for pdf in pdf_list:\n",
    "        merger.append(pdf)\n",
    "\n",
    "    merger.write(OP_path+\"result.pdf\")\n",
    "    merger.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef55ed66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc6f31bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# deleting extra pdfs\n",
    "#for j in range (len(pdf_list)):\n",
    "#    os.remove(OP_path+str(j)+'.pdf')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07df0702",
   "metadata": {},
   "source": [
    "FOR PDF\n",
    "1. function to get Meta data of I/P folder (no of files and file types)\n",
    "    -> how many pages are there in each PDF (sepearte dictionary or somethng)\n",
    "2. Converting/saving each pdf into a given location (finalized loaction directory) \n",
    "3. leave image file types, create a seperate directory inside finalized dierctory and save it as others\n",
    "4. each pdf should have diferrent folder.\n",
    "5. initialize the class handler with hthe i/p and o/p directories"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72893723",
   "metadata": {},
   "source": [
    "FOR IMAGES\n",
    "1. collating every image into a single PDF folder wise (output_dir/pdfs/pdf1), slug\n",
    "2. not the page numbers to avoid incorrect collation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07d75076",
   "metadata": {},
   "source": [
    "Seperate function to extract the metadata of the folder contents (file types, file size,...)\n",
    "\n",
    "Given a folder, extract metatdata, covert all documents into various differnt formats (pdf<-> img)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27184699",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b9bc6363",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Get_Started_With_Smallpdf.pdf\n",
      "sample.pdf\n",
      "sample1.pdf\n",
      "sample2.pdf\n",
      "sample3.pdf\n"
     ]
    }
   ],
   "source": [
    "#Folder Metadata Extraction\n",
    "\n",
    "from pathlib import Path\n",
    " \n",
    "path = Path(r\"C:\\Users\\tonum\\OneDrive\\Desktop\\Codes\\Images_to_PDF\\Sample_PDF_Data\")\n",
    "files_in_path = path.iterdir()\n",
    "for item in files_in_path:\n",
    "    if item.is_file():\n",
    "        print(item.name)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "28566019",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Image Metadata Extraction\n",
    "\n",
    "import os\n",
    "from PIL import Image\n",
    "from PIL.ExifTags import TAGS\n",
    "\n",
    "IP_path = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/Jpeg\"\n",
    "\n",
    "img_list = [os.path.join(IP_path, file)\n",
    "        for file in os.listdir(IP_path)\n",
    "        if file.endswith('.jpg')]\n",
    "\n",
    "for i in img_list:\n",
    "    image = Image.open(i)\n",
    "    \n",
    "    # extracting the exif metadata\n",
    "    exifdata = image.getexif()\n",
    "    \n",
    "# looping through all the tags present in exifdata\n",
    "for tagid in exifdata:\n",
    "    \n",
    "    # getting the tag name instead of tag id\n",
    "    tagname = TAGS.get(tagid, tagid)\n",
    "\n",
    "    # passing the tagid to get its respective value\n",
    "    value = exifdata.get(tagid)\n",
    "\n",
    "    # printing the final result\n",
    "    print(f\"{tagname:25}: {value}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5468908",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d7faa4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# PDF Metadata Extraction\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "72e4ee7a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----Metadata of the file----\n",
      "/Title:0\n",
      "/CreationDate:D:20220608172847Z\n",
      "/ModDate:D:20220608172847Z\n"
     ]
    }
   ],
   "source": [
    "import PyPDF2\n",
    "\n",
    "filename = \"C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/PDF/0.pdf\"\n",
    "\n",
    "pdfFile = PyPDF2.PdfFileReader(filename,'rb')\n",
    "data = pdfFile.getDocumentInfo()\n",
    "\n",
    "print(\"----Metadata of the file----\")\n",
    "\n",
    "for metadata in data:\n",
    "    print(metadata+ \":\" +data[metadata])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "322a2c11",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c0b0666",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
