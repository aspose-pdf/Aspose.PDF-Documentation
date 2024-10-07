---
title: Qué hay de nuevo
linktitle: Qué hay de nuevo
type: docs
weight: 10
url: /net/whatsnew/
description: En esta página se presentan las características nuevas más populares en Aspose.PDF para .NET que se han introducido en las últimas versiones.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## Qué hay de nuevo en Aspose.PDF 24.8

Conversión de documentos PDF al formato PDF/A-4

Desde la versión 24.8, ha sido posible convertir documentos PDF a PDF/A-4. La Parte 4 del estándar, basada en PDF 2.0, fue publicada a finales de 2020.

El siguiente fragmento de código demuestra cómo convertir un documento al formato PDF/A-4, asumiendo que el documento de entrada es PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // Solo los documentos PDF-2.x pueden ser convertidos a PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
El segundo fragmento de código muestra cómo convertir un documento a formato PDF/A-4 cuando el documento de entrada es una versión anterior.

```cs
    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.Convert(Stream.Null, PdfFormat.v_2_0, ConvertErrorAction.Delete);

        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```

Desde 24.8 hemos introducido un método para aplanar el contenido transparente en documentos PDF:

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## Novedades en Aspose.PDF 24.7

Comparando documentos PDF con Aspose.PDF para .NET

Desde 24.7 es posible comparar el contenido de documentos PDF con marcas de anotación y salida lado a lado:

El primer fragmento de código muestra cómo comparar las primeras páginas de dos documentos PDF.
El primer fragmento de código demuestra cómo comparar las primeras páginas de dos documentos PDF.

```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

El segundo fragmento de código amplía el alcance para comparar el contenido completo de dos documentos PDF.

```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```
## Qué hay de nuevo en Aspose.PDF 24.4

Esta versión admite la aplicación de una máscara de recorte a imágenes:

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

Desde 24.4 puedes seleccionar la fuente de papel por tamaño de página PDF en el diálogo de impresión usando la API

A partir de Aspose.PDF 24.4 esta preferencia puede ser activada o desactivada usando la propiedad Document.PickTrayByPdfSize o la fachada PdfContentEditor:

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("¡Hola mundo!"));

        // Establece la bandera para elegir una bandeja de papel usando el tamaño de página PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs
    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // Establece la bandera para elegir una bandeja de papel usando el tamaño de página del PDF
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

Desde esta versión se añadió el complemento Aspose.PDF Signature para .NET:

- Ejemplo con la creación de un nuevo campo y opciones:

```cs

    // crear Firma
    var plugin = new Signature();
    // crear objeto SignOptions para establecer instrucciones
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // añadir ruta del archivo de entrada
    opt.AddInput(new FileDataSource(inputPath));
    // establecer ruta del archivo de salida
    opt.AddOutput(new FileDataSource(outputPath));
    // establecer opciones adicionales
    opt.Reason = "mi Motivo";
    opt.Contact = "mi Contacto";
    opt.Location = "mi Ubicación";
    // realizar el proceso
    plugin.Process(opt);
```

- Ejemplo con un campo existente vacío

```cs

    // crear Firma
    var plugin = new Signature();
    // crear objeto SignOptions para establecer instrucciones
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // añadir ruta del archivo de entrada con campo de firma vacío
    opt.AddInput(new FileDataSource(inputPath));
    // establecer ruta del archivo de salida
    opt.AddOutput(new FileDataSource(outputPath));
    // establecer nombre del campo de firma existente
    opt.Name = "Signature1";
    // realizar el proceso
    plugin.Process(opt);
```
## Novedades en Aspose.PDF 24.3

Desde esta versión se añadió el plugin PDF/A Converter para .NET:

```cs
    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // Agrega el archivo fuente
    options.AddInput(new FileDataSource("ruta_a_tu_archivo_pdf.pdf")); // reemplazar con la ruta de tu archivo real

    // Agrega la ruta para guardar el archivo convertido
    options.AddOutput(new FileDataSource("ruta_al_archivo_convertido.pdf"));

    // Crea la instancia del plugin
    var plugin = new PdfAConverter();

    // Ejecuta la conversión
    plugin.Process(options);
```

- Implementa una búsqueda a través de una lista de frases en un TextFragmentAbsorber:

```cs
    var regexes = new Regex[]
    {
    new Regex(@"(?s)documento\s+(?:(?:no\(?s?\)?\.?)|(?:número(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|y)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Parcela[\s\r\n]+de:?", RegexOptions.IgnoreCase),
    new Regex(@"titularidad[\s\r\n]+en", RegexOptions.IgnoreCase),
    new Regex("Titularidad en:", RegexOptions.IgnoreCase),
    new Regex(@"archivo.?[\s\r\n]+(?:nos?|números?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"archivo.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };
    var document = new Document(input);
    var absorber = new TextFragmentAbsorber(
    regexes,
    new TextSearchOptions(true)
    );
    document.Pages.Accept(absorber);
    // Obtener resultado
    var result = absorber.RegexResults
```
Desde la versión 24.3 es posible agregar un campo de firma vacío en cada página al archivo PDF/A

```cs
    static void Main(string[] args)
    {
        try
        {
            var lic = new Aspose.Pdf.License();
            lic.SetLicense("Aspose.Total.lic");

            string source = "source.pdf";
            string fieldName = "signature_1234";
            string dest = "source_fieldNotInAllPages.pdf";
            addFieldSingle_NewCode(source, dest, fieldName, 1);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }
        Console.ReadLine(); 
    }

    private static void addFieldSingle_NewCode(string source, string dest, string fieldName, int page)
    {
        File.Copy(source, dest, true);
        using (var fs = new FileStream(dest, FileMode.Open))
        {
            // El nuevo código sugerido, usando el objeto SignatureField (este código funciona bien)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // Añadir la apariencia predeterminada para el campo de firma
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // ¿Cómo hacer ahora visible newAddedField en todas las páginas?
            Aspose.Pdf.Annotations.Annotation addedField = null;
            foreach (Aspose.Pdf.Annotations.Annotation a in doc.Pages[1].Annotations)
            {
            if (a.FullName == fieldName)
                {
                    addedField = a;
                    break;
                }
            }
            if (addedField != null)
            {
                for (int p = 1; p <= doc.Pages.Count; p++)
                {
                    if (p == page) continue;
                    doc.Pages[p].Annotations.Add(addedField);
                }
            }

            doc.Save();
        }
        System.Diagnostics.Process.Start(dest);
    }
```
## Qué hay de nuevo en Aspose.PDF 24.2

Desde la versión 24.2 es posible obtener los datos vectoriales de un archivo PDF

Se implementó GraphicsAbsorber para obtener datos vectoriales de documentos:

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## Qué hay de nuevo en Aspose.PDF 24.1

Desde el lanzamiento de la versión 24.1 es posible importar anotaciones en formato FDF a PDF:

```cs
    var fdfPath = Params.InputPath + "50745.fdf";
    var templatePath = Params.InputPath + "Empty.pdf";
    var outputPath = Params.OutputPath + "50745_form.pdf";

    using (var form = new Aspose.Pdf.Facades.Form(templatePath))
    {
        using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
        {
            form.ImportFdf(fdfInputStream);
        }

        form.Save(outputPath);
    }
```

También, soporta el acceso al Diccionario de Páginas o al Catálogo de Documentos.
También, soporta el acceso al Diccionario de Páginas o al Catálogo de Documentos.

Aquí hay ejemplos de código para DictionaryEditor:

- Añadir nuevos valores

```cs

    // ejemplo de nombres de claves
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    var outputPath = "page_dictionary_editor.pdf";
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new CosPdfName("datos de nombre"));
        dictionaryEditor.Add(KEY_STRING, new CosPdfString("datos de cadena"));
        dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

        doc.Save(outputPath);
    }
```

- Añadir y establecer valores al diccionario

```cs

    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Nombre antiguo"));
        // o 
        dictionaryEditor[KEY_NAME] = new CosPdfName("Nombre nuevo");
    }
```
- Obtener valor del diccionario

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // o
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- Eliminar valor del diccionario

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## Novedades en Aspose.PDF 23.12

El formulario se puede encontrar y el texto se puede reemplazar utilizando el siguiente fragmento de código:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var absorber = new TextFragmentAbsorber();
            absorber.Visit(form);

            foreach (var fragment in absorber.TextFragments)
            {
                fragment.Text = "";
            }
        }
    }

    document.Save(output);
```            

O, el formulario se puede eliminar completamente:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    for (int i = 1; i <= forms.Count; i++)
    {
        if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
        {
            forms.Delete(forms[i].Name);
        }
    }

    document.Save(output);
```            

Otra variante de eliminar el formulario:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var name = forms.GetFormName(form);
            forms.Delete(name);
        }
    }

    document.Save(output);
``` 

- Todos los formularios se pueden eliminar utilizando el siguiente fragmento de código:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- Implementar la conversión de PDF a Markdown:

```cs
    string markdownOutputFilePath = "output.md"
    string inputPdfPath = "input.pdf"
    using (Document doc = new Document(inputPdfPath))
    {
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    doc.Save(markdownOutputFilePath, saveOptions);
    }
```

- Implementar la conversión de OFD a PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

Desde esta versión se añadió el plugin de Merger:

```cs
    // Ruta al archivo PDF fusionado de salida.
    var outputPath = "TestMerge.pdf";

    // Crear una nueva instancia de Merger.
    var merger = new Merger();

    // Crear MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // Procesar la fusión de PDFs.
    merger.Process(opt);
```

Además, desde esta versión se añadió el plugin de ChatGPT:
También, desde esta versión se añadió el plugin de ChatGPT:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Añade la ruta del archivo de salida.
    options.ApiKey = "Tu clave API."; // Debes proporcionar la clave para acceder a la API.
    options.MaxTokens = 1000; // El número máximo de tokens para generar en la finalización del chat.

    // Añade los mensajes de solicitud.
    options.Messages.Add(new Message
    {
        Content = "Eres un asistente útil.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "¿Cuál es el diámetro de la pizza más grande que se ha hecho?",
        Role = Role.User
    });

    // Procesa la solicitud.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // El objeto de finalización del chat de la API ChatGPT.
    }
```

## Novedades en Aspose.PDF 23.11
## Qué hay de nuevo en Aspose.PDF 23.11

Desde esta versión es posible eliminar texto oculto de un archivo PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // Esta opción puede usarse para prevenir que otros fragmentos de texto se muevan después del reemplazo de texto oculto.
        textAbsorber.TextReplaceOptions = new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None);

        document.Pages.Accept(textAbsorber);

        foreach (var fragment in textAbsorber.TextFragments)
        {
            if (fragment.TextState.Invisible)
            {
                fragment.Text = "";
            }
        }

        document.Save(outputFile);
```

Desde 23.11 se soporta la interrupción de hilos:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //esto es un texto largo, se usó Lorem Ipsum de 8350 caracteres para provocar una suspensión
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // El tiempo de espera debe ser menor al tiempo requerido para guardar el documento completo (sin interrupción).
            Thread.Sleep(500);

            // Interrumpir el proceso
            monitor.Interrupt();

            // Esperar por la interrupción...
            thread.Join();
        }
        private class RowSpanWorker
        {
            private readonly string outputPath;
            private readonly InterruptMonitor monitor;

            public RowSpanWorker(string outputPath, InterruptMonitor monitor)
            {
                this.outputPath = outputPath;
                this.monitor = monitor;
            }
            public void Work()
            {
                string text = InterruptMonitorTests.LongText;
                using (var doc = new Document())
                {
                    InterruptMonitor.ThreadLocalInstance = this.monitor;
                    var page = doc.Pages.Add();

                    var table = new Aspose.Pdf.Table
                    {
                        DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, 0.1F)
                    };

                    var row0 = table.Rows.Add();

                    // añadir una celda que abarca dos filas y contiene un texto muy largo
                    var cell00 = row0.Cells.Add(text);
                    cell00.RowSpan = 2;
                    cell00.IsWordWrapped = true;
                    row0.Cells.Add("Ipsum Ipsum Ipsum Ipsum Ipsum Ipsum ");
                    row0.Cells.Add("Dolor Dolor Dolor Dolor Dolor Dolor ");

                    var row1 = table.Rows.Add();
                    row1.Cells.Add("IpsumDolor Dolor Dolor Dolor Dolor ");
                    row1.Cells.Add("DolorDolor Dolor Dolor Dolor Dolor ");

                    page.Paragraphs.Add(table);

                    try
                    {
                        doc.Save(this.outputPath);
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine(ex.Message);
                    }
                }
            }
        }
    }
```
## Novedades en Aspose.PDF 23.10

La actualización actual presenta tres versiones de Eliminación de etiquetas de PDFs etiquetados.

- Eliminar algún elemento de nodo de un documentElement (elemento raíz del árbol):

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // elemento eliminado
        document.Save(outputPath);
    }

    // También puedes eliminar el structElement mismo
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- Eliminar todas las etiquetas de elementos marcados del documento, pero mantener los elementos de la estructura:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var root = structure.Children[0];
    var queue = new Queue<Element>();
    queue.Enqueue(root);
    while(queue.TryDequeue(out var element))
    {
        foreach (var child in element.Children)
        {
            queue.Enqueue(child);
        }

        if (element is TextElement || element is FigureElement)
        {
            element.Remove();
        }
    }
```
- Eliminar etiquetas completamente:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

Desde el 23.10 se implementó una nueva característica para medir la altura del carácter. Utiliza el siguiente código para medir la altura de un carácter.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

Ten en cuenta que la medición se basa en la fuente incrustada en el documento. Si falta alguna información para una dimensión, este método devuelve 0.

Además, esta versión proporciona la firma de un PDF usando un HASH firmado:

```cs
    public void PDFNET_54566()
    {
        var inputPdf = "54566.pdf";
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        var outputPdf = "54566_out.pdf";
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(inputPdf);
            var pkcs7 = new PKCS7(inputP12, inputPfxPassword);
            pkcs7.CustomSignHash = CustomSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
            sign.Save(outputPdf);
        }
        using (var sign = new PdfFileSignature())
        {
            sign.BindPdf(outputPdf);
            Assert.IsTrue(sign.VerifySignature("Signature1"));
        }
    }

    private byte[] CustomSignHash(byte[] signableHash)
    {
        var inputP12 = "54566.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
```
Una nueva característica más es la Escalación de Página en la Configuración de Diálogo de Impresión:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## Qué hay de nuevo en Aspose.PDF 23.9

Desde 23.9 soporte para eliminar una anotación hija de un campo rellenable.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation .PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## Qué hay de nuevo en Aspose.PDF 23.8

Desde 23.8 soporte para añadir detección de Actualizaciones Incrementales.

La función para detectar Actualizaciones Incrementales en un documento PDF ha sido añadida. Esta función devuelve 'true' si un documento fue guardado con actualizaciones incrementales; de lo contrario, devuelve 'false'.

```cs

    var path = "C:\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

Además, 23.8 soporta las maneras de trabajar con campos de casilla de verificación anidados.
También, 23.8 soporta las formas de trabajar con campos de casillas de verificación anidadas.

- Crear campo de casilla de verificación de múltiples valores:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Establecer el valor de la primera opción del grupo de casillas de verificación
    checkbox.ExportValue = "opción 1";

    // Añadir nueva opción justo debajo de las existentes
    checkbox.AddOption("opción 2");

    // Añadir nueva opción en el rectángulo dado
    checkbox.AddOption("opción 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Seleccionar la casilla de verificación añadida
    checkbox.Value = "opción 2";
    document.Save("checkbox_group.pdf");
    }
```

- Obtener y establecer el valor de una casilla de verificación de múltiples valores:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Los valores permitidos se pueden recuperar de la colección AllowedStates
    // Establecer el valor de la casilla usando la propiedad Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // el valor previamente establecido, por ejemplo, "opción 1"

    // El valor debe ser cualquier elemento de AllowedStates
    checkbox.Value = "opción 2";
    checkboxValue = checkbox.Value; // opción 2

    // Desmarcar casillas estableciendo Value en "Off" o Checked en false
    checkbox.Value = "Off";
    // o, alternativamente:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## Qué hay de nuevo en Aspose.PDF 23.7

Desde Aspose.PDF 23.7 se soporta la adición de la extracción de formas:

```cs

    public void PDFNET_46298()
    {
        var input1 = "46298_1.pdf";
        var input2 = "46298_2.pdf";

        var source = new Document(input1);
        var dest = new Document(input2);

        var graphicAbsorber = new GraphicsAbsorber();
        graphicAbsorber.Visit(source.Pages[1]);
        var area = new Rectangle(90, 250, 300, 400);
        dest.Pages[1].AddGraphics(graphicAbsorber.Elements, area);
    }
```

También soporta la capacidad de detectar desbordamiento al agregar texto:

```cs

    var doc = new Document();
    var paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    var rectangle = new Rectangle(100, 600, 500, 700, false);
    var paragraph = new TextParagraph();
    var fragment = new TextFragment(paragraphContent);
    paragraph.VerticalAlignment = VerticalAlignment.Top;
    paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
    paragraph.Rectangle = rectangle;
    var isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.TextState.FontSize -= 0.5f;
        isFitRectangle = fragment.TextState.IsFitRectangle(paragraphContent, rectangle);
    }
    paragraph.AppendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.Pages.Add());
    builder.AppendParagraph(paragraph);
    doc.Save(output);
```
## Qué hay de nuevo en Aspose.PDF 23.6

Desde Aspose.PDF 23.6 soporte para agregar los siguientes complementos:

- Aspose PdfConverter de HTML a PDF
- Aspose PdfOrganizer API de Redimensionamiento
- Aspose PdfOrganizer API de Compresión

Actualizar el Aspose.PdfForm
- agregar característica 'Exportar "Valores de los campos en el documento a archivo CSV"
- agregar la capacidad de establecer propiedades para campos individuales

También soporte para agregar la capacidad de establecer el título de la página HTML, Epub:

```cs

    var document = new Document(Params.InputPath + "53357.pdf");

    var htmlSaveOptions = new HtmlSaveOptions
    {
        ExplicitListOfSavedPages = new[] { 1 },
        SplitIntoPages = false,
        FixedLayout = true,
        CompressSvgGraphicsIfAny = false,
        SaveTransparentTexts = true,
        SaveShadowedTextsAsTransparentTexts = true,
        FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsWOFF,
        RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground,
        PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml,
        Title = "Título para la página"   // <-- esto se agregó
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```
## ¿Qué hay de nuevo en Aspose.PDF 23.5?

Desde la versión 23.5 se soporta la opción de tamaño de fuente en RedactionAnnotation. Utiliza el siguiente fragmento de código para resolver esta tarea:

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // Crear instancia de RedactionAnnotation para una región específica de la página
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // Texto a imprimir en la anotación de redacción
    annot.OverlayText = "(Desconocido)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // Repetir texto de superposición sobre la anotación de redacción
    annot.Repeat = false;
    // ¡Nueva propiedad aquí!
    annot.FontSize = 20;
    // Añadir la anotación a la colección de anotaciones de la primera página
    doc.Pages[1].Annotations.Add(annot);
    // Aplana la anotación y redacta el contenido de la página (es decir, elimina texto e imagen
    // bajo la anotación redactada)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## Novedades en Aspose.PDF 23.4

Aspose.PDF anunció el lanzamiento del SDK .NET 7.

## Novedades en Aspose.PDF 23.3.1

Desde Aspose.PDF 23.3 se soporta agregar los siguientes plugins:

- Aspose.PdfForm
- Aspose.PdfConverter PDF a HTML
- Aspose.PdfConverter PDF a XLSX
- Aspose.PdfOrganizer Rotar
- Aspose.PdfExtrator para Imágenes

## Novedades en Aspose.PDF 23.3

La versión 23.3 introdujo soporte para agregar una resolución a una imagen. Se pueden usar dos métodos para resolver este problema:

```cs
    var table = new Table
            {
                ColumnWidths = "600"
            };

            for(var j = 0; j < 2; j ++)
            {
                var row = table.Rows.Add();
                var cell = row.Cells.Add();
                cell.Paragraphs.Add(new Image()
                {
                    IsApplyResolution = true,
                    File = imageFile
                });
            }

            page.Paragraphs.Add(table);
```

Y el segundo enfoque:

```cs
    page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
            page.Paragraphs.Add(new Image()
            {
                IsApplyResolution = true,
                File = imageFile
            });
```
La imagen se colocará con resolución escalada o puede establecer las propiedades FixedWidth o FixedHeight en combinación con IsApplyResolution

## Novedades en Aspose.PDF 23.1.1

Desde Aspose.PDF 23.1.1 se ofrece soporte para agregar los siguientes plugins:

- Plugin Aspose.PdfOrganizer
- Plugin Aspose.PdfExtractor

## Novedades en Aspose.PDF 23.1

Desde la versión 23.1 se ofrece soporte para crear la anotación PrinterMark.

Las marcas de impresión son símbolos gráficos o texto agregado a una página para ayudar al personal de producción a identificar los componentes de un trabajo de múltiples placas y mantener una salida consistente durante la producción. Ejemplos comúnmente utilizados en la industria de la impresión incluyen:

- Objetivos de registro para alinear placas
- Rampas grises y barras de color para medir colores y densidades de tinta
- Marcas de corte que muestran dónde debe recortarse el medio de salida

Mostraremos el ejemplo de la opción con barras de color para medir colores y densidades de tinta.
Mostraremos el ejemplo de la opción con barras de color para medir colores y densidades de tinta.

```cs
var outFile = myDir + "ColorBarTest.pdf");

using (var doc = new Document())
{
    Page page = doc.Pages.Add();
    page.TrimBox = new Aspose.Pdf.Rectangle(20, 20, 580, 820);
    AddAnnotations(page);
    doc.Save(outFile);
}

void AddAnnotations(Page page)
{
    var rectBlack = new Aspose.Pdf.Rectangle(100, 300, 300, 320);
    var rectCyan = new Aspose.Pdf.Rectangle(200, 600, 260, 690);
    var rectMagenta = new Aspose.Pdf.Rectangle(10, 650, 140, 670);

    var colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    var colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    var colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.ColorOfCMYK = ColorsOfCMYK.Magenta;
    var colorBarYellow = new ColorBarAnnotation(page, new Aspose.Pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.Annotations.Add(colorBarBlack);
    page.Annotations.Add(colorBarCyan);
    page.Annotations.Add(colorBaMagenta);
    page.Annotations.Add(colorBarYellow);
}
```
También admite la extracción de imágenes vectoriales. Intente usar el siguiente código para detectar y extraer gráficos vectoriales:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## Novedades en Aspose.PDF 22.12

Desde esta versión se admite la conversión de PDF a imagen DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## Novedades en Aspose.PDF 22.09

Desde 22.09 se admite agregar propiedad para modificar el orden de las rubricas del sujeto (E=, CN=, O=, OU=, ) en la firma.

```cs
    using (var fileSign = new PdfFileSignature())
    {
        fileSign.BindPdf(inputPdf);
        var rect = new System.Drawing.Rectangle(100, 100, 400, 100);
        var signature = new PKCS7Detached(inputPfx, "123456789");
        signature.CustomAppearance = new SignatureCustomAppearance()
        {
            UseDigitalSubjectFormat = true,
            DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.CN, SubjectNameElements.O }
            //o
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## ¿Qué hay de nuevo en Aspose.PDF 22.6

Desde 22.5 soporte para extraer texto Subíndice y Superíndice de PDF.

Si el documento PDF contiene texto Subíndice y Superíndice como H2O, entonces la extracción del texto del PDF también debe extraer su información de formato (en el texto plano extraído).
Si el PDF contiene texto en cursiva, también debe incluirse en el contenido extraído.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## ¿Qué hay de nuevo en Aspose.PDF 22.4

Esta versión incluye información para Aspose.PDF para .NET:

- PDF a ODS: Reconocer texto en subíndice y superíndice;

**ejemplo**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods", options);
```

- PDF a XMLSpreadSheet2003: Reconocer texto en subíndice y superíndice;

- PDF a Excel: Reconocer texto en subíndice y superíndice;
- PDF a Excel: Reconocer texto en subíndice y superíndice;

- Eliminar firmas UR al guardar el documento;

- Eliminar la bandera de Sospechosos en MarkInfo al guardar el documento;

- Eliminar Información al guardar el documento

## Qué hay de nuevo en Aspose.PDF 22.3

Esta versión incluye las siguientes actualizaciones:

- Soporte para AFRelationship;

- Validación del encabezado PDF;

- Eliminar el subfiltro adbe.x509.rsa_sha1 al guardar el documento;

- Formatear campo como Número y Formato de Fecha;

- Prohibir el uso de cifrado RC4 en FDF 2.0ю

## Qué hay de nuevo en Aspose.PDF 22.2

Desde la versión 22.2 es posible firmar un documento utilizando PdfFileSignature con LTV, y con la capacidad de cambiar el hash de SHA1 a SHA256.

```csharp
Ejemplo de uso:
var inputPdf = "51168.pdf";
var inputPfx = "51168.pfx";
var inputPfxPassword = "111111";
var outputPdf = "51168.pdf";

using (var doc = new Document(inputPdf))
{
    using (PdfFileSignature signature = new PdfFileSignature(doc))
    {
        var pkcs = new PKCS7(inputPfx, inputPfxPassword)
        {
            UseLtv = true,
            TimestampSettings = new TimestampSettings("http://freetsa.org/tsr", string.Empty, DigestHashAlgorithm.Sha256)
        };
        signature.Sign(1, false, new System.Drawing.Rectangle(300, 100, 1, 1), pkcs);
        signature.Save(outputPdf);
    }
}
```
## Qué hay de nuevo en Aspose.PDF 22.1

Ahora, Aspose.PDF para .NET admite la carga de documentos desde uno de los formatos de documento más populares, Formato de Documento Portátil (PDF) versión 2.0.

## Qué hay de nuevo en Aspose.PDF 21.11

### Permitir caracteres no latinos en la contraseña

```csharp
Aspose.Pdf.Facades.PdfFileSecurity fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity();
fileSecurity.AllowExceptions = true;
    try
{
 fileSecurity.BindPdf(exportDoc);
 bool res = fileSecurity.EncryptFile("æøå", "æøå", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256, Aspose.Pdf.Facades.Algorithm.AES);
 Console.WriteLine(res);
 fileSecurity.Save(output("encrypted.pdf"));
}
    catch(Exception e)
{
    Console.WriteLn("Exception: " + e.Message);
}
```

## Qué hay de nuevo en Aspose.PDF 21.10

### ¿Cómo detectar texto oculto?

Por favor, use TextState.Invisible para obtener información sobre la invisibilidad del texto fuera de la configuración del modo de renderizado.

Usamos el siguiente código para la prueba:

```csharp
Document pdf = new Document(dataDir + "TestPage.pdf");
Console.WriteLine(pdf.FileName);
var page = pdf.Pages[1];
var textFragmentAbsorber = new TextFragmentAbsorber();
page.Accept(textFragmentAbsorber);
var textFragmentCollection = textFragmentAbsorber.TextFragments;
for (int i = 1; i <= textFragmentCollection.Count; i++)
{
    TextFragment fragment = textFragmentCollection[i];
    Console.WriteLine("Fragmento {0} en {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Texto: {0}", fragment.Text);
    Console.WriteLine("Modo de Renderizado: {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibilidad: {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```
### ¿Cómo obtener información sobre el número de capas en un documento PDF?

```csharp
Please use code snippet:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## Lo nuevo en Aspose.PDF 21.9

Personaliza el color de fondo para la apariencia de la firma y el color de la fuente de las etiquetas en el área de la firma con Aspose.PDF para .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//set colors
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## Lo nuevo en Aspose.PDF 21.8

### ¿Cómo cambiar el color del texto en la Firma Digital?

En la versión 21.8 propiedad ForegroundColor, permite cambiar el color del texto en la Firma Digital.

```csharp
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //crear un rectángulo para la ubicación de la firma
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//establecer color de texto
        ForegroundColor = Color.Green
    };
    // firmar el archivo PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //guardar el archivo PDF de salida
    pdfSign.Save(outFile);
}
```

## Novedades en Aspose.PDF 21.7

### Creación de PDF basada en XML y XLS con parámetros

Para agregar parámetros XSL necesitamos crear nuestra propia [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) y configurarla como propiedad en [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). El siguiente fragmento muestra cómo usar esta clase con los archivos de muestra descritos arriba.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Ejemplo de uso de XsltArgumentList
         XsltArgumentList argsList = new XsltArgumentList();
        argsList.AddParam("isBoldName", "", "yes");
        //---------------------

        var pdfDocument = new Aspose.Pdf.Document(TransformXml(XmlContent, XsltContent, argsList), options);
        pdfDocument.Save(_dataDir + "data_xml.pdf");
    }

 public static MemoryStream TransformXml(string inputXml, string xsltString, XsltArgumentList argsList=null)
    {
            var transform = new XslCompiledTransform();
            using (var reader = XmlReader.Create(new StringReader(xsltString)))
            {
                transform.Load(reader);
            }
            var memoryStream = new MemoryStream();

            var results = new StreamWriter(memoryStream);
            using (var reader = XmlReader.Create(new StringReader(inputXml)))
            {
                transform.Transform(reader, argsList, results);
            }

            memoryStream.Position = 0;
            return memoryStream;
    }
```
## Qué hay de nuevo en Aspose.PDF 21.6

Con Aspose.PDF para .NET puedes ocultar imágenes usando ImagePlacementAbsorber del documento:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // Ocultar imagen en la primera página
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## Qué hay de nuevo en Aspose.PDF 21.5

### ¿Cómo extraer el nombre completo de la fuente de su descripción/recurso en PDF?

Puedes obtener una fuente completa con el prefijo con la propiedad BaseFont para la clase Font.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"nombre de fuente : {font.FontName} nombre de BaseFont : {font.BaseFont}");
}
pdf.Dispose();
```

## Qué hay de nuevo en Aspose.PDF 21.4

### Añadir API para fusionar imágenes

Aspose.PDF 21.4 te permite combinar imágenes.
Aspose.PDF 21.4 te permite combinar imágenes.

```csharp
private static void MergeAsJpeg()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.jpg", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\49616_600.jpg", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream =
                 PdfConverter.MergeImages(inputImagesStreams, ImageFormat.Jpeg, ImageMergeMode.Vertical, 1, 1))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.jpg", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```
## ¿Qué hay de nuevo en Aspose.PDF 21.3

### Exposición pública de la propiedad para detectar la Protección de Información de Azure

También puede fusionar sus imágenes en formato Tiff:

```csharp
private static void MergeAsTiff()
{
   List<Stream> inputImagesStreams = new List<Stream>();
   using (FileStream inputFile300dpi = new FileStream(@"c:\300.tiff", FileMode.Open))
   {
       inputImagesStreams.Add(inputFile300dpi);
       using (FileStream inputFile600dpi = new FileStream(@"c:\600.tiff", FileMode.Open))
       {
           inputImagesStreams.Add(inputFile600dpi);
           using (Stream inputStream = PdfConverter.MergeImagesAsTiff(inputImagesStreams))
           {
               using (FileStream outputStream = new FileStream(@"c:\out.tiff", FileMode.Create))
               {
                   byte[] buffer = new byte[32768];
                   int read;
                   while ((read = inputStream.Read(buffer, 0, buffer.Length)) > 0)
                   {
                       outputStream.Write(buffer, 0, read);
                   }
               }
           }
       }
    }
}
```
### Exposición pública de propiedades para detectar la Protección de Información de Azure

Con el siguiente fragmento de código, deberías poder acceder al contenido cifrado de tus archivos PDF, protegidos con Protección de Información de Azure:

```csharp
 public void Azure_Information_Protection()
 {
     string inputFile = @"c:\pdf.pdf";
     Document document = new Document(inputFile);
     if (document.EmbeddedFiles[1].AFRelationship == AFRelationship.EncryptedPayload)
     {
            if (document.EmbeddedFiles[1].EncryptedPayload != null)
            {
              // document.EmbeddedFiles[1].EncryptedPayload.Type == "EncryptedPayload"
              // document.EmbeddedFiles[1].EncryptedPayload.Subtype == "MicrosoftIRMServices"
              // document.EmbeddedFiles[1].EncryptedPayload.Version == "2"
            }
     }
}
```

## Novedades en Aspose.PDF 21.1

### Agregar soporte para recuperar el color de fondo de TextFragment

En esta versión de Aspose.PDF, se ha habilitado la función para recuperar el color de fondo.
En esta versión de Aspose.PDF, se ha habilitado la función para recuperar el color de fondo.

Por favor, considere el siguiente código:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Aceptar el absorber para todas las páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Iterar a través de los fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texto: '{0}'", textFragment.Text);
    Console.WriteLine("Color de fondo: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("Color de frente: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Color de fondo del segmento: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### Después de la conversión a HTML, la fuente está completamente incrustada en el resultado

También, en Aspose.PDF 21.1, después de convertir PDF a HTML, se hizo disponible la inclusión de fuentes en el documento HTML resultante. Es posible con la nueva opción booleana de guardado HtmlSaveParameter.SaveFullFont.

Aquí está el fragmento de código:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
