---
title: Converter Imagem para PDF em Python
linktitle: Converter Imagem para arquivo PDF
type: docs
weight: 10
url: pt/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: Este tópico mostra como converter Imagem para PDF usando Aspose.PDF para Python via biblioteca C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Nossa biblioteca demonstra trechos de código para converter os formatos de imagem mais populares - JPEG. Você pode converter imagens JPG para PDF com Aspose.PDF para Python via C++ seguindo os passos:

## Converter Imagem para PDF

Você pode converter imagens JPG para PDF com Aspose.PDF para C++ seguindo os passos:

1. Abra o arquivo de imagem de entrada usando a biblioteca PIL
1. Obtenha a largura e altura da imagem
1. Crie uma nova instância de Documento usando a biblioteca AsposePDFPythonWrappers
1. Defina a altura e largura fixas da imagem
1. Adicione uma nova página ao documento
1. Adicione a imagem à página
1. Salve o PDF de saída com o método 'document.save'.

O trecho de código abaixo mostra como converter Imagem JPG para PDF usando Python via C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Defina o caminho do diretório para os arquivos de dados
dataDir = os.path.join(os.getcwd(), "samples")

# Defina o caminho do arquivo de entrada
input_file = os.path.join(dataDir, "sample.jpg")

# Defina o caminho do arquivo de saída
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Abra o arquivo de imagem de entrada usando a biblioteca PIL
pil_img = Image.open(input_file)

# Obtenha a largura e a altura da imagem
width, height = pil_img.size

# Crie uma nova instância de Document usando a biblioteca AsposePDFPythonWrappers
document = apw.Document()

# Crie uma nova instância de Image usando a biblioteca AsposePDFPythonWrappers
image = apw.Image()

# Defina o caminho do arquivo da imagem
image.file = input_file

# Defina a altura e largura fixas da imagem
image.fix_height = height
image.fix_width = width

# Adicione uma nova página ao documento
page = document.pages.add()

# Adicione a imagem à página
page.paragraphs.add(image)

# Salve o documento no caminho do arquivo de saída
document.save(output_file)
```