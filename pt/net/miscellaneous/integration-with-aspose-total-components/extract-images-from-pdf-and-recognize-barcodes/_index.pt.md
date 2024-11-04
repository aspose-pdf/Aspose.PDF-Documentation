---
title: Extrair Imagens de PDF e Reconhecer Códigos de Barras
type: docs
weight: 20
url: /net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Os documentos PDF geralmente são compostos por Texto, Imagem, Tabela, Anexos, Gráfico, Anotação e outros objetos relacionados. Existem casos em que Códigos de Barras estão embutidos dentro do arquivo PDF e alguns clientes têm a necessidade de identificar os Códigos de Barras presentes dentro do arquivo PDF. O seguinte artigo explica os passos sobre como extrair imagens das páginas de PDF e identificar os Códigos de Barras nelas.

{{% /alert %}}

De acordo com o Document Object Model do Aspose.PDF para .NET, um arquivo PDF contém uma ou mais páginas onde cada página contém uma coleção de Imagens, Formulários e Fontes no objeto Resources.
De acordo com o Document Object Model do Aspose.PDF para .NET, um arquivo PDF contém uma ou mais páginas onde cada página contém uma coleção de Imagens, Formulários e Fontes no objeto Recursos.

**C#**

```csharp

//abrir documento
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// percorrer as páginas individuais do arquivo PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // percorrer cada imagem extraída das páginas do PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //salvar imagem de saída
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // definir a posição do stream para o início do Stream
            imageStream.Position = 0;
   
            // Instanciar objeto BarCodeReader
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // obter texto do BarCode da imagem do BarCode
                string code = barcodeReader.GetCodeText();
   
                // escrever o texto do BarCode na saída do Console
                Console.WriteLine("BARCODE : " + code);
            }
   
            // fechar objeto BarCodeReader para liberar o arquivo de imagem
   
            barcodeReader.Close();
        }
    }
}

```
Para obter mais detalhes sobre os tópicos abordados neste artigo, por favor visite os seguintes links

- [Extrair Imagens do Arquivo PDF](/net/extract-images-from-the-pdf-file/)
- [Ler Códigos de Barras](https://docs.aspose.com/barcode/net/read-barcodes/)
