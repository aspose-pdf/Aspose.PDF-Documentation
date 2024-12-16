---
title: Extraer Imágenes de PDF 
linktitle: Extraer Imágenes de PDF
type: docs
weight: 20
url: /es/cpp/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Además, una tarea demandada al trabajar con documentos PDF es extraer imágenes de un archivo PDF. Por ejemplo, recibiste un correo electrónico en PDF con muchas imágenes geniales que te gustaría extraer como archivos separados.

La biblioteca Aspose.PDF te permite extraer imágenes de PDF con el siguiente fragmento de código:

```cpp
void ExtractImage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Parsing\\");

    // Cadena para el nombre del archivo
    String infilename("sample-image.pdf");
    String outfilename("extracted_image.jpeg");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Extraer una imagen particular
    auto xImage = document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->idx_get(1);

    auto outputImage = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Guardar imagen de salida
    xImage->Save(outputImage, System::Drawing::Imaging::ImageFormat::get_Jpeg());
    outputImage->Close();

    std::clog << __func__ << ": Finish" << std::endl;
}
```