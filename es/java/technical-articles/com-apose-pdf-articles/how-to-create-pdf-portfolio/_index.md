---
title: Cómo Crear un Portafolio PDF
type: docs
weight: 10
url: es/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Los portafolios PDF te permiten reunir contenido de una variedad de fuentes (por ejemplo, archivos PDF, Word, Excel, JPEG) en un único contenedor unificado. Los archivos originales conservan sus identidades individuales pero se ensamblan en un archivo de portafolio PDF. Los usuarios pueden abrir, leer, editar y formatear cada archivo componente de manera independiente de los otros archivos componentes.

Aspose.PDF para Java permite la creación de documentos de Portafolio PDF usando la clase Document. Carga el archivo individual en un objeto FileSpecification y añádelos al objeto Document.Collection usando el método add(...). Una vez que los archivos han sido añadidos, usa el método save(..) de la clase Document para generar el documento de portafolio.

{{% /alert %}}

## Ejemplo de Código

El siguiente ejemplo usa un archivo Microsoft XPS, un documento de Word, un PDF y un archivo de imagen para crear un Portafolio PDF.

**Un portafolio PDF creado con Aspose.PDF**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}