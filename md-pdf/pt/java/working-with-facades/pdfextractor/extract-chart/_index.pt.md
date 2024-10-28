---
title: Extrair objetos de gráfico de documento PDF (facades)
type: docs
weight: 20
url: /java/extract-chart-objects/
description: Esta seção explica como extrair objetos de gráfico de PDFs com Aspose.PDF Facades usando a Classe PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extrair objetos de gráfico de documento PDF (facades)

O PDF permite agrupar o conteúdo da página em elementos chamados de **Conteúdo Marcado**. O Adobe Acrobat os mostra como "containers". Os objetos de gráfico são colocados nesses objetos. Introduzimos um novo método extractMarkedContentAsImages() na classe PdfExtractor para extrair esses objetos. Este método renderiza cada **Conteúdo Marcado** em uma imagem separada. Por favor, note que todos os gráficos não estão totalmente colocados em um container. Por causa disso, alguns gráficos serão salvos em imagens separadas por partes.

Por favor, note que o agrupamento correto de conteúdo em containers é responsabilidade do designer do documento PDF.
 Se você quiser obter gráficos com cabeçalho ou outros objetos, deverá editar/criar o documento PDF onde todo o gráfico está colocado em um único contêiner.

```java

 //Abrir documento

Document document = new Document("sample.pdf");

//instanciar PdfExtractor

PdfExtractor pdfExtractor = new PdfExtractor();

//Extrair objetos de gráfico como imagem em uma pasta

pdfExtractor.extractMarkedContentAsImages(document.getPages().get_Item(1), "C:/Temp/Charts_page_1");

document.close();
```