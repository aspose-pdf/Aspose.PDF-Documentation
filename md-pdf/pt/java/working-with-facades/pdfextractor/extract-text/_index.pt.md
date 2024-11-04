---
title: Extrair Imagens de PDF (facades)
type: docs
weight: 30
url: /java/extract-images/
description: Esta seção explica como extrair imagens com Aspose.PDF Facades usando a Classe PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A classe [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) permite que você extraia imagens de um arquivo PDF.
 Primeiro, você precisa criar um objeto da classe [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) e vincular o arquivo PDF de entrada usando o método bindPdf. Depois disso, chame o método [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) para extrair todas as imagens para a memória. Uma vez que as imagens são extraídas, você pode obtê-las com a ajuda dos métodos hasNextImage e getNextImage. Você precisa iterar por todas as imagens extraídas usando um loop while. Para salvar as imagens no disco, você pode chamar a sobrecarga do método getNextImage que leva o caminho do arquivo como argumento. O trecho de código a seguir mostra como extrair imagens do PDF inteiro para arquivos.

```java
public static void ExtractImages()
{
    //Crie um extrator e vincule-o ao documento
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Execute o extrator
    extractor.extractImage();
    int imageNumber = 1;
    //Iterar através da coleção de imagens extraídas
    while (extractor.hasNextImage())
    {
        //Recuperar imagem da coleção e salvá-la em um arquivo
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++), ImageType.getPng());
    }
}
```