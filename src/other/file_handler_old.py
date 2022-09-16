{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5e8b5991",
   "metadata": {},
   "source": [
    "## Notebook to find the metadata of all Images and PDF documents in a folder & convert popular different Image file types into PDF and Vice-Versa"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "99bfbf48",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing Dependencies for file handling\n",
    "from PIL import Image\n",
    "from pdf2image import convert_from_path\n",
    "from PyPDF2 import PdfFileMerger\n",
    "from PyPDF2 import PdfFileReader\n",
    "\n",
    "import os\n",
    "import os.path\n",
    "\n",
    "# Importing Dependencies for Metadata Extraction\n",
    "from hachoir.parser import createParser\n",
    "from hachoir.metadata import extractMetadata"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e6ea3bf9",
   "metadata": {},
   "source": [
    "#### PDF to Image Coversion Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "83f8b1d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class pdf2Img_convertor:\n",
    "    \n",
    "    def __init__ (self, path, path1):\n",
    "        self.path = path\n",
    "        self.path1 = path1\n",
    "          \n",
    "    \n",
    "    def pdf_2_jpg(self):\n",
    "        \n",
    "        pdf_list = [self.path + '/'+f \n",
    "                     for f in os.listdir(self.path) \n",
    "                     if os.path.isfile(os.path.join(self.path, f))]\n",
    "        \n",
    "        print(\"Number of PDF=\"+str(len(pdf_list)))\n",
    "        \n",
    "#         pdf_list = [os.path.join(ip_path, f)\n",
    "#                 for f in os.listdir(ip_path)\n",
    "#                 if f.endswith('.pdf')]\n",
    "\n",
    "        # Counting the number of pages in each pdf and converting the pages into image\n",
    "        for file in pdf_list:\n",
    "            images = convert_from_path(file)\n",
    "            i = 1\n",
    "            length = len(images)\n",
    "\n",
    "            print(\"Number of pages in PDF=\"+str(length))\n",
    "\n",
    "        for image in images:\n",
    "            image.save(self.path1 + str(i) + '.jpg', 'Jpeg')\n",
    "            i = i + 1\n",
    "            \n",
    "    \n",
    "    def pdf_2_png(self):\n",
    "        \n",
    "        pdf_list = [os.path.join(self.path, f) \n",
    "                     for f in os.listdir(self.path) \n",
    "                     if os.path.isfile(os.path.join(self.path, f))]\n",
    "\n",
    "#         pdf_list = [os.path.join(ip_path, f)\n",
    "#                     for f in os.listdir(ip_path)\n",
    "#                     if f.endswith('.pdf')]\n",
    "\n",
    "        # Counting the number of pages in each pdf and converting the pages into image\n",
    "        for file in pdf_list:\n",
    "            images = convert_from_path(file)\n",
    "            i = 1\n",
    "            length = len(images)\n",
    "\n",
    "            print(\"Number of pages in PDF=\"+str(length))\n",
    "\n",
    "        for image in images:\n",
    "            image.save(self.path1 + str(i) + '.png', 'png')\n",
    "            i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9507ce5d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of pages in PDF=1\n"
     ]
    }
   ],
   "source": [
    "#pdf2Img_convertor(IP_file)\n",
    "\n",
    "ip_path = 'C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/PDF/'\n",
    "op_path = 'C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/png/'\n",
    "\n",
    "convertor = pdf2Img_convertor(ip_path, op_path)\n",
    "\n",
    "convertor.pdf_2_png()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a808fe57",
   "metadata": {},
   "source": [
    "#### Images to PDF Coversion Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c151f4a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Img2pdf_convertor:\n",
    "    \n",
    "        \n",
    "    def __init__ (self, path, path1):\n",
    "        self.path = path\n",
    "        self.path1 = path1\n",
    "        \n",
    "    #PNG to PDF Conversion Function\n",
    "    def png_2_pdf(self):\n",
    "                \n",
    "        file_list = [os.path.join(self.path, f) \n",
    "                     for f in os.listdir(self.path) \n",
    "                     if os.path.isfile(os.path.join(self.path, f))]\n",
    "        \n",
    "#         for file in file_list:\n",
    "#             if file.endswith('.pdf'):\n",
    "#                 self.pdf_metadata(file)\n",
    "        \n",
    "        img_list = [os.path.join(self.path, file)\n",
    "                for file in os.listdir(self.path)\n",
    "                if file.endswith('.png')]\n",
    "        \n",
    "        print(\"Number of Images=\"+str(len(img_list)))\n",
    "\n",
    "        for i,path in enumerate(img_list):\n",
    "            image_1 = Image.open(path)\n",
    "            im_1 = image_1.convert('RGB')\n",
    "            im_1.save(self.path1+str(i)+'.pdf') \n",
    "        \n",
    "    #JPEG to PDF Conversion Function    \n",
    "    def jpg_2_pdf(self):\n",
    "\n",
    "        img_list = [os.path.join(self.path, file)\n",
    "                for file in os.listdir(self.path)\n",
    "                if file.endswith('.jpg')]\n",
    "        \n",
    "        print(\"Number of Images=\"+str(len(img_list)))\n",
    "\n",
    "        for i,path in enumerate(img_list):\n",
    "            new_image_1 = Image.open(path)\n",
    "            new_im_1 = new_image_1.convert('RGB')\n",
    "            new_im_1.save(self.path1+str(i)+'.pdf')\n",
    "    \n",
    "    # fuction to merge all pdfs into a single pdf in a given folder\n",
    "    def merge_pdf():\n",
    "\n",
    "        pdf_list = [os.path.join(self.path1, file)\n",
    "                for file in os.listdir(self.path1)\n",
    "                if file.endswith('.pdf')]\n",
    "\n",
    "        merger = PdfFileMerger()\n",
    "\n",
    "        for pdf in pdf_list:\n",
    "            \n",
    "            if not os.path.exists('my_folder'):\n",
    "                os.makedirs('my_folder')\n",
    "            merger.append(pdf)\n",
    "\n",
    "        merger.write('my_folder/result.pdf')\n",
    "        merger.close()\n",
    "        \n",
    "        # deleting extra pdfs\n",
    "        for j in range (len(pdf_list)):\n",
    "            os.remove(self.path1+str(j)+'.pdf')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "96adec03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of Images=1\n"
     ]
    }
   ],
   "source": [
    "ip_path = 'C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/png/'\n",
    "op_path = 'C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/PDF/'\n",
    "\n",
    "convertor = Img2pdf_convertor(ip_path, op_path)\n",
    "convertor.png_2_pdf()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "995ce959",
   "metadata": {},
   "source": [
    "#### MetaData Extraction Class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3c2ccc86",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Metadata_extraction:\n",
    "    \n",
    "    def __init__ (self, path):\n",
    "        self.path = path\n",
    "        \n",
    "    \n",
    "    def meta_extractor(self):\n",
    "\n",
    "        \n",
    "        file_list = [os.path.join(self.path, f) \n",
    "                     for f in os.listdir(IP_path) \n",
    "                     if os.path.isfile(os.path.join(IP_path, f))]\n",
    "        \n",
    "        for file in file_list:\n",
    "            if file.endswith('.pdf'):\n",
    "                self.pdf_metadata(file)\n",
    "                \n",
    "                #self.convert_bytes(os.path.getsize(file))\n",
    "                y = convert_bytes(os.path.getsize(file))\n",
    "                print('File size: ' + y)\n",
    "                \n",
    "                print('\\n')\n",
    "            else:\n",
    "                self.image_metadata(file)\n",
    "                #self.convert_bytes(os.path.getsize(file))\n",
    "                \n",
    "                y = convert_bytes(os.path.getsize(file))\n",
    "                print('File size: ' + y)\n",
    "                \n",
    "                print('\\n')\n",
    "            \n",
    "    # Size Conversion\n",
    "    def convert_bytes(self, size):\n",
    "\n",
    "        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:\n",
    "            if size < 1024.0:\n",
    "                return \"%3.1f %s\" % (size, x)\n",
    "            size /= 1024.0\n",
    "            \n",
    "    # Image Metadata Extraction\n",
    "    def image_metadata(self, filename):\n",
    "        \n",
    "      #  for filename in img_list:\n",
    "        parser = createParser(filename)\n",
    "        metadata = extractMetadata(parser)\n",
    "        metadata = metadata.exportPlaintext()\n",
    "\n",
    "        print('Metadata of Image: ' + filename)\n",
    "        \n",
    "        for fields in metadata:\n",
    "            print(fields)\n",
    "                \n",
    "        #######################################################################\n",
    "        \n",
    "    # PDF Metadata Extraction\n",
    "    def pdf_metadata(self, filename):\n",
    "\n",
    "        pdf = PdfFileReader(filename)\n",
    "        info = pdf.getDocumentInfo()\n",
    "        \n",
    "        print('Metadata of Document: ' + filename)\n",
    "        \n",
    "        for fields in info:\n",
    "            print(fields+ \":\" + str(info[fields]))  \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38e0642c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 438,
   "id": "12141de9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Metadata of Document: C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/Get_Started_With_Smallpdf.pdf\n",
      "/CreationDate:D:20201014170810+02'00'\n",
      "/Creator:Adobe InDesign 15.1 (Macintosh)\n",
      "/ModDate:D:20201014170810+02'00'\n",
      "/Producer:Adobe PDF Library 15.0\n",
      "/Trapped:/False\n",
      "File size: 67.8 KB\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[warn] Skip value width_dpi=0 (filter)\n",
      "[warn] Skip value height_dpi=0 (filter)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Metadata of Image: C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/OIP.jpg\n",
      "Metadata:\n",
      "- Image width: 474 pixels\n",
      "- Image height: 355 pixels\n",
      "- Bits/pixel: 24\n",
      "- Pixel format: YCbCr\n",
      "- Compression: JPEG (Baseline)\n",
      "- Comment: JPEG quality: 69%\n",
      "- Format version: JFIF 1.01\n",
      "- MIME type: image/jpeg\n",
      "- Endianness: Big endian\n",
      "File size: 32.5 KB\n",
      "\n",
      "\n",
      "Metadata of Image: C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/Rotated.png\n",
      "Metadata:\n",
      "- Image width: 514 pixels\n",
      "- Image height: 640 pixels\n",
      "- Bits/pixel: 24\n",
      "- Pixel format: RGB\n",
      "- Compression rate: 2.2x\n",
      "- Compression: deflate\n",
      "- MIME type: image/png\n",
      "- Endianness: Big endian\n",
      "File size: 434.4 KB\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "IP_file = 'C:/Users/tonum/OneDrive/Desktop/Codes/Images_to_PDF/Image/'\n",
    "meta = Metadata_extraction(IP_file)\n",
    "MetaData = meta.meta_extractor()\n",
    "MetaData"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f55255fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb2af36c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adcf2c81",
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
