---
title: Rotación del sello alrededor del punto central
type: docs
weight: 10
url: /net/rotating-stamp-about-the-center-point/
description: Esta sección explica cómo rotar el sello alrededor del punto central usando la Clase Stamp.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

El [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/net/) te permite agregar un sello en un archivo PDF existente. A veces, los usuarios necesitan rotar el sello. En este artículo, veremos cómo rotar un sello alrededor de su punto central.

{{% /alert %}}

## Detalles de la implementación

La clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) te permite agregar una marca de agua en un archivo PDF. Puedes especificar la imagen para ser añadida como un sello usando el método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). El método [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) te permite establecer el origen del sello añadido; este origen son las coordenadas inferiores izquierda del sello. También puedes establecer el tamaño de la imagen usando el método [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Ahora, vemos cómo se puede rotar el sello alrededor del centro del sello. [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) clase proporciona una propiedad llamada Rotation. Esta propiedad establece o obtiene la rotación de 0 a 360 del contenido del sello. Podemos especificar cualquier valor de rotación de 0 a 360. Al especificar el valor de rotación, podemos rotar el sello sobre su punto central. Si un Stamp es un objeto del tipo Stamp, entonces el valor de rotación puede especificarse como aStamp.Rotation = 90. En este caso, el sello se rotará a 90 grados sobre el centro del contenido del sello. El siguiente fragmento de código le muestra cómo rotar el sello sobre el punto central:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-RotatingStamp-RotatingStamp.cs" >}}