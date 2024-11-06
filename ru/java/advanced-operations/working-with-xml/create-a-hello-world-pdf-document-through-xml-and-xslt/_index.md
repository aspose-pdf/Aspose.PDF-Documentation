---
title: Создание PDF документа Hello World с использованием XML и XSLT
linktitle: Создание PDF документа Hello World с использованием XML и XSLT
type: docs
weight: 10
url: ru/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: Aspose.PDF для Java предоставляет возможность преобразовать XML файл в PDF документ, требуя, чтобы входной XML файл соответствовал Aspose.PDF XSD Java Schema.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Иногда у вас могут быть существующие XML файлы, содержащие данные приложения, и вы хотите создать PDF отчет, используя эти файлы. Вы можете использовать XSLT для преобразования вашего существующего XML документа в совместимый с Aspose.Pdf XML документ, а затем создать PDF файл. Существует 3 шага для создания PDF с использованием XML и XSLT.

Пожалуйста, выполните следующие шаги для преобразования XML файла в PDF документ с помощью XSLT:

* Создайте экземпляр класса PDF, который представляет PDF документ

* Если вы приобрели лицензию, то вы также должны встроить код для использования этой лицензии с помощью класса License в пространстве имен Aspose.Pdf
* Свяжите входные файлы XML и XSLT с экземпляром класса PDF, вызвав его метод BindXML
* Сохраните связанный XML с экземпляром PDF как PDF-документ

## Входной XML файл

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Привет, мир!</Content>
</Contents>
```

## Входной XSLT файл

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```


## Создание Hello World с использованием XML и Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      // Привязываем XML и XSLT файлы
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      // Сохраняем PDF документ
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```