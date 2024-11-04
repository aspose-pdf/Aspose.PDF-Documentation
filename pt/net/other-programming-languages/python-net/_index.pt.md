---
title: Usando Aspose.PDF para .NET com Python
linktitle: Integração com Python
type: docs
weight: 100
url: /net/python-net/
description: Neste tutorial, você explorará as diferentes maneiras de criar e modificar arquivos PDF em Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

Este artigo descreve breves exemplos de como criar PDF usando a integração do Aspose.PDF para .NET com Python.

## Pré-requisitos

Para usar Aspose.PDF para .NET em Python, por favor, use o seguinte `requirments.txt`:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

Também, você deve colocar `Aspose.PDF.dll` na pasta desejada.

## Criando um PDF Simples usando Python

Para trabalhar, precisaremos integrar o [PythonNet](https://github.com/pythonnet/pythonnet) à nossa aplicação e fazer algumas configurações.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### Gerar documento simples

Vamos criar um PDF simples com o texto clássico "Hello, world". Para uma explicação mais detalhada, por favor siga para [esta página](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Inicializar o objeto de documento
        document = Document()
        # Adicionar página
        page = document.Pages.Add()
        # Adicionar texto à nova página
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Criar objeto TextBuilder
        textBuilder = TextBuilder(page)

        # Anexar o fragmento de texto à página PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Criando PDF Complexo usando Python

Os próximos exemplos mostram como podemos criar um documento PDF complexo com imagens e tabelas. Este exemplo é baseado na [página seguinte](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self, licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... omitido ...

    # Criar um Documento Complexo
    def run_complex(self):

        # Inicializar objeto do documento
        document = Document()
        # Adicionar página
        page = document.Pages.Add()

        # Adicionar imagem
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Adicionar Cabeçalho
        header = TextFragment("Novas rotas de ferry no Outono de 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Adicionar descrição
        descriptionText = "Os visitantes devem comprar bilhetes online e os bilhetes são limitados a 5.000 por dia. \
        O serviço de ferry está operando com metade da capacidade e em um horário reduzido. Espere filas."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # Adicionar tabela
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Cidade de Partida")
        headerRow.Cells.Add("Ilha de Partida")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## Como executar a geração de PDFs no Windows

Este trecho mostra como executar os exemplos acima em um PC Windows. Supomos que a `class HelloWorld` esteja localizada no arquivo `example_get_started.py`.
Se você executar a versão de teste do Aspose.PDF para .NET, você deve passar uma string vazia como `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```

