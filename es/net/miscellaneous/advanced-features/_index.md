---
title: Características Avanzadas
type: docs
weight: 210
url: es/net/advanced-features/
---

## Enviando Pdf al Navegador para Descarga

A veces, cuando estás desarrollando una aplicación ASP.NET, necesitas enviar archivos PDF a navegadores web para que se descarguen sin guardarlos físicamente. Para lograr esto, puedes guardar el documento PDF en un objeto MemoryStream después de generarlo y pasar los bytes de ese MemoryStream al objeto Response. Hacer esto hará que el navegador descargue el documento PDF generado.

El siguiente fragmento de código demuestra la funcionalidad anterior:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-Examples.Web-SendPdfToBrowserForDownload.aspx-1.cs" >}}

## Extrayendo archivos incrustados de un archivo PDF

Aspose.PDF se destaca cuando se trata de características avanzadas para trabajar con archivos de formato PDF. Extrae archivos incrustados mucho mejor que otras herramientas que ofrecen esta característica.

Con Aspose.PDF para .NET, puedes extraer eficientemente cualquier archivo incrustado, ya sea una fuente incrustada, una imagen, un video o un audio.
Con Aspose.PDF para .NET, puedes extraer de manera eficiente cualquier archivo incrustado que puede ser una fuente incrustada, una imagen, un video o un audio.

El siguiente fragmento de código extrae todos los archivos incrustados de un archivo PDF:

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-DocumentConversion-PDFToXML-PDFToXML.cs" >}}

## Uso de Script Latex para Agregar Expresiones Matemáticas

Con Aspose.PDF, puedes agregar expresiones/formulas matemáticas dentro de un documento PDF usando script latex. Los siguientes ejemplos muestran cómo se puede utilizar esta característica de dos maneras diferentes, para agregar una fórmula matemática dentro de una celda de tabla:

### Sin preámbulo y ambiente de documento

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript-WithoutPreambleanddocument.cs" >}}

### Con preámbulo y ambiente de documento

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Text-UseLatexScript2-WithPreambleanddocument.cs" >}}

### Soporte para Etiquetas Latex
### Soporte para Etiquetas Latex

El entorno align está definido en el paquete amsmath, y el entorno proof está definido en el paquete amsthm. Por lo tanto, debes especificar estos paquetes usando el comando \usepackage en el preámbulo del documento. Y esto significa que debes encerrar el texto LaTeX en el entorno del documento, como se muestra en el siguiente ejemplo de código.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Text-UseLatexScript3-UseLatexScript3.cs" >}}
