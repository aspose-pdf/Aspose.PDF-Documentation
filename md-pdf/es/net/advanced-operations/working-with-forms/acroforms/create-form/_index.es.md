---
title: Create AcroForm - Create Fillable PDF in C#
linktitle: Create AcroForm
type: docs
weight: 10
url: /net/create-form/
description: Con Aspose.PDF para .NET puede crear un formulario desde cero en su archivo PDF
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm",
    "alternativeHeadline": "Cómo crear AcroForm en PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, create acroform",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Con Aspose.PDF para .NET puede crear un formulario desde cero en su archivo PDF"
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Crear formulario desde cero

### Agregar campo de formulario en un documento PDF

La clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) proporciona una colección llamada [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) que te ayuda a gestionar campos de formulario en un documento PDF.

Para agregar un campo de formulario:

1. Crea el campo de formulario que deseas agregar.
1. Llama al método Add de la colección [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### Agregando TextBoxField

El siguiente ejemplo muestra cómo agregar un [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Crear un campo
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Agregar campo al documento
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Guardar PDF modificado
pdfDocument.Save(dataDir);
```
### Añadiendo RadioButtonField

Los siguientes fragmentos de código muestran cómo agregar [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) en un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Instancia el objeto Document
Document pdfDocument = new Document();
// Añade una página al archivo PDF
pdfDocument.Pages.Add();
// Instancia el objeto RadioButtonField con el número de página como argumento
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Añade la primera opción de botón de radio y también especifica su origen usando el objeto Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Añade la segunda opción de botón de radio
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Añade el botón de radio al objeto de formulario del objeto Document
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Guarda el archivo PDF
pdfDocument.Save(dataDir);
```
El siguiente fragmento de código muestra los pasos para agregar RadioButtonField con tres opciones y colocarlos dentro de las celdas de una tabla.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// Guardar el archivo PDF
doc.Save(dataDir);
```
### Agregando Etiqueta a RadioButtonField

El siguiente fragmento de código muestra cómo agregar una etiqueta que se asociará con RadioButtonField:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar el formulario PDF fuente
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // Crear objeto TextParagraph
        TextParagraph par = new TextParagraph();

        // Establecer la posición del párrafo
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Especificar el modo de ajuste de palabras
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Agregar nuevo TextFragment al párrafo
        par.AppendLine(updatedFragment);

        // Agregar el TextParagraph usando TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### Añadiendo campo ComboBox

Los siguientes fragmentos de código muestran cómo agregar un campo ComboBox en un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Crear objeto Document
Document doc = new Document();

// Añadir página al objeto documento
doc.Pages.Add();

// Instanciar objeto ComboBox Field
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Añadir opción al ComboBox
combo.AddOption("Rojo");
combo.AddOption("Amarillo");
combo.AddOption("Verde");
combo.AddOption("Azul");

// Añadir objeto combo box a la colección de campos de formulario del objeto documento
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Guardar el documento PDF
doc.Save(dataDir);
```

### Añadir Tooltip a Campo de Formulario

La clase Document proporciona una colección denominada Form que gestiona los campos de formulario en un documento PDF.
La clase Document proporciona una colección llamada Form que gestiona los campos de formulario en un documento PDF.

Los fragmentos de código que siguen muestran cómo agregar un mensaje de ayuda a un campo de formulario, primero usando C# y luego Visual Basic.

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Cargar el formulario PDF fuente
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Establecer el mensaje de ayuda para el campo de texto
(doc.Form["textbox1"] as Field).AlternateName = "Mensaje de ayuda del cuadro de texto";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Guardar el documento actualizado
doc.Save(dataDir);
```

changefreq: "monthly"
type: docs

