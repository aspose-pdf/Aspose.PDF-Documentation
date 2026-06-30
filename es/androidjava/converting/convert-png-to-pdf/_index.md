---
title: Convertir PNG a PDF
linktitle: Convertir PNG a PDF
type: docs
weight: 200
url: /es/androidjava/convert-png-to-pdf/
lastmod: "2026-06-30"
description: Este artículo muestra cómo convertir PNG a PDF con la biblioteca Aspose.PDF en su Android mediante aplicaciones Java. Puede convertir imágenes PNG al formato PDF utilizando pasos sencillos.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Android via Java** soporta la función de convertir imágenes PNG a formato PDF. Revise el siguiente fragmento de código para realizar su tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen raster que usa compresión sin pérdidas, lo que lo hace popular entre sus usuarios.

Puede convertir PNG a una imagen PDF utilizando los siguientes pasos:

1. Cargue la imagen PNG de entrada
1. Leer los valores de altura y anchura
1. Crear un nuevo documento y agregar una página
1. Establecer dimensiones de la página
1. Guardar el archivo de salida

Además, el fragmento de código a continuación muestra cómo convertir PNG a PDF en sus aplicaciones Java:

```java
    public void convertPNGtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```

