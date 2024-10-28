---
title: Cómo firmar digitalmente un PDF
linktitle: Firmar digitalmente PDF
type: docs
weight: 10
url: /cpp/digitally-sign-pdf-file/
description: Firmar digitalmente documentos PDF usando C++. Verificar o validar los PDFs firmados digitalmente usando C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Firmar PDF con firmas digitales

Puede firmar el documento PDF para confirmar su contenido, o puede aprobar el documento con Aspose.PDF.

Aspose.PDF para C++ admite la función de firmar digitalmente los archivos PDF utilizando la clase SignatureField. También puede certificar un archivo PDF con un certificado PKCS12. Algo similar a [Agregar firmas y seguridad en Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Use la clase [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) para firmar su PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// Cadena para el nombre de la ruta.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Usar PKCS7/PKCS7Detached
























// objetos

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Guardar archivo PDF de salida

signature->Save(outFile);
}
```

## Añadir marca de tiempo a la firma digital

### Cómo firmar digitalmente un PDF con marca de tiempo

Aspose.PDF para C++ admite firmar digitalmente el PDF con un servidor de marca de tiempo o servicio web.

Las marcas de tiempo se utilizan para indicar la fecha y la hora en que firmó el documento. El sellado de tiempo fiable demuestra que el contenido de sus PDFs existía en un momento específico y no ha cambiado desde entonces.

Utilice la clase [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) para agregar una marca de tiempo de confianza a las firmas digitales o documentos.

Por favor, eche un vistazo al siguiente fragmento de código que obtiene la marca de tiempo y la agrega al documento PDF:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// Cadena para el nombre de la ruta.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // Usuario/Contraseña pueden
























// ser omitidos

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// Crear cualquiera de los tres tipos de firma

signature->Sign(1, u"Razón de la Firma", u"Contacto", u"Ubicación", true, rect, pkcs);

// Guardar archivo PDF de salida

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```