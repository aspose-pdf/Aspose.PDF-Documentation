---
title: Migración desde la versión Pre 4.x.x de Aspose.PDF para Java
type: docs
weight: 20
url: /java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Se ha lanzado una nueva versión autoportada de Aspose.PDF para Java y ahora este único producto admite la capacidad de generar documentos PDF desde cero, así como también proporciona la capacidad de manipular documentos PDF existentes.

{{% /alert %}}

## Binarios del producto

{{% alert color="primary" %}}

En la primera versión (v4.0.0), estamos enviando dos archivos jar, es decir, **aspose.pdf-3.3.0.jdk15.jar** y **aspose.pdf-new-4.0.0.jar**.

- **aspose.pdf-3.3.0.jdk14.jar**

Este archivo jar es la misma versión de producto que está disponible actualmente bajo el módulo de descarga con el título [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx). En adelante, vamos a llamar a esta versión de lanzamiento como Aspose.PDF for Java legado. En este primer lanzamiento, los usuarios existentes de Aspose.PDF for Java podrían no verse afectados porque obtienen la misma versión de lanzamiento. Sin embargo, en algún momento, vamos a eliminar este archivo jar separado y todas las clases y enumeraciones de Aspose.PDF for Java legado (pre 4.x.x) estarán disponibles bajo el paquete com.aspose.pdf.generator de un único archivo aspose.pdf-new-4.x.x.jar.
- **aspose.pdf-new-4.0.0.jar**
  Este archivo jar es una nueva versión auto-portada de Aspose.PDF para .NET a la plataforma Java.
 Este archivo jar contiene el nuevo Modelo de Objeto de Documento (DOM) para crear y también manipular archivos PDF existentes, así como el actual Aspose.PDF.Kit para Java. Todas las clases y enumeraciones de Aspose.PDF.Kit para Java están agrupadas bajo el paquete com.aspose.pdf.facades y en el tercer trimestre de 2013, Aspose.PDF.Kit para Java será descontinuado. Por lo tanto, animamos a nuestros actuales clientes de Aspose.PDF.Kit para Java a intentar migrar su código a la nueva versión autoportada.

Por favor, revisa la siguiente entrada de blog para obtener más información sobre la Estructura de Aspose.PDF autoportado para Java.