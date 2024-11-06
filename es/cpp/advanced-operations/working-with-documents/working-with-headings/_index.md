---
title: Working with Headings in PDF
type: docs
weight: 90
url: es/cpp/working-with-headings/
lastmod: "2021-11-11"
description: Crear numeración en el encabezado de su documento PDF con C++. Aspose.PDF para C++ muestra diferentes tipos de estilos de numeración.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aplicar Estilo de Numeración en el Encabezado

Cualquier texto en un documento comienza con un encabezado. Los encabezados son una parte integral del contenido, independientemente del estilo y tema.
Los encabezados ayudan a llamar la atención sobre el texto y ayudan a los usuarios a encontrar la información que necesitan en el documento, mejorando la legibilidad y la percepción visual. Usando estilos de encabezado, también puede crear rápidamente una tabla de contenido, cambiar la estructura del documento.
Entonces, veamos cómo trabajar con encabezados usando la biblioteca Aspose.PDF para C++.

[Aspose.PDF para C++](/pdf/cpp/) ofrece muchos estilos de numeración predefinidos. Estas estilos de numeración predefinidos están almacenados en una enumeración, NumberingStyle. Los valores predefinidos de la enumeración NumberingStyle y sus descripciones se dan a continuación:

|**Tipos de encabezado**|**Descripción**|
| :- | :- |
|NumeralsArabic|Tipo árabe, por ejemplo, 1,1.1,...|
|NumeralsRomanUppercase|Tipo romano mayúsculas, por ejemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculas, por ejemplo, i,i.ii, ...|
|LettersUppercase|Tipo inglés mayúsculas, por ejemplo, A,A.B, ...|
|LettersLowercase|Tipo inglés minúsculas, por ejemplo, a,a.b, ...|
La propiedad **Style** de la clase **Aspose.PDF.Heading** se utiliza para establecer los estilos de numeración de los encabezados.

|**Figura: Estilos de numeración predefinidos**|
| :- |
El código fuente, para obtener la salida mostrada en la figura anterior, se proporciona a continuación en el ejemplo.

```cpp
void WorkingWithHeadingsInPDF() {
    // String para nombre de ruta
    String _dataDir("C:\\Samples\\");

    // String para nombre de archivo de entrada
    String outputFileName("ApplyNumberStyle_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"List 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"List 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"el valor, a partir de la fecha efectiva del plan, de la propiedad que se distribuirá bajo el plan debido a cada permitido");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // Guardar archivo de salida concatenado
    document->Save(_dataDir + outputFileName);
}
```