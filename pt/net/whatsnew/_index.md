---
title: O que há de novo
linktitle: O que há de novo
type: docs
weight: 10
url: pt/net/whatsnew/
description: Esta página apresenta as novidades mais populares em Aspose.PDF para .NET que foram introduzidas nas últimas versões.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2024-09-06"
---

## O que há de novo no Aspose.PDF 24.8

Convertendo documentos PDF para o formato PDF/A-4

Desde a versão 24.8, tornou-se possível converter documentos PDF para PDF/A-4. A parte 4 do padrão, baseada no PDF 2.0, foi publicada no final de 2020.

O seguinte trecho de código demonstra como converter um documento para o formato PDF/A-4, assumindo que o documento de entrada é PDF 2.x.

```cs

    string documentPath = "";
    string conversionLogPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        // Apenas documentos PDF-2.x podem ser convertidos para PDF/A-4
        document.Convert(conversionLogPath, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
        document.Save(resultPdfPath);
    }
```
O segundo trecho de código demonstra como converter um documento para o formato PDF/A-4 quando o documento de entrada é uma versão anterior.

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

Desde 24.8 introduzimos um método para achatar conteúdo transparente em documentos PDF:

```cs
    string documentPath = "";
    string resultPdfPath ="";

    using (var document = new Document(documentPath))
    {
        document.FlattenTransparency();
        document.Save(resultPdfPath);
    }
```

## O que há de novo no Aspose.PDF 24.7

Comparando Documentos PDF com Aspose.PDF para .NET

Desde 24.7 é possível comparar o conteúdo de documentos PDF com marcas de anotação e saída lado a lado:

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF.
O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF.

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

O segundo trecho de código expande o escopo para comparar todo o conteúdo de dois documentos PDF.

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
## O que há de novo no Aspose.PDF 24.4

Esta versão suporta a aplicação de uma máscara de recorte em imagens:

```cs
    Document doc = new Document("input.pdf");
    using (var fs1 = new FileStream("mask1.jpg", FileMode.Open))
    using (var fs2 = new FileStream("mask2.png", FileMode.Open))
    {
        doc.Pages[1].Resources.Images[1].AddStencilMask(fs1);
        doc.Pages[1].Resources.Images[2].AddStencilMask(fs2);
    }
```

Desde o 24.4 você pode selecionar a fonte de papel por tamanho de página PDF na caixa de diálogo de impressão usando a API

A partir do Aspose.PDF 24.4, essa preferência pode ser ativada e desativada usando a propriedade Document.PickTrayByPdfSize ou a fachada PdfContentEditor:

```cs
    using (Document document = new Document())
    {
        Page page = document.Pages.Add();
        page.Paragraphs.Add(new TextFragment("Olá mundo!"));

        // Define a bandeira para escolher uma bandeja de papel usando o tamanho da página PDF
        document.PickTrayByPdfSize = true;
        document.Save("result.pdf");
    }
```
```cs
    using (PdfContentEditor contentEditor = new PdfContentEditor())
    {
        contentEditor.BindPdf("input.pdf");

        // Define a bandeja de papel a ser escolhida com base no tamanho da página do PDF
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
        contentEditor.Save("result.pdf");
    }
```

A partir desta versão foi adicionado o plugin Aspose.PDF Signature para .NET:

- Exemplo com criação de novo campo e opções:

```cs

    // criar Assinatura
    var plugin = new Signature();
    // criar objeto SignOptions para definir instruções
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // adicionar caminho do arquivo de entrada
    opt.AddInput(new FileDataSource(inputPath));
    // definir caminho do arquivo de saída
    opt.AddOutput(new FileDataSource(outputPath));
    // definir opções extras
    opt.Reason = "meu Motivo";
    opt.Contact = "meu Contato";
    opt.Location = "meu Local";
    // executar o processo
    plugin.Process(opt);
```

- Exemplo com campo existente vazio

```cs

    // criar Assinatura
    var plugin = new Signature();
    // criar objeto SignOptions para definir instruções
    var opt = new SignOptions(inputPfxPath, inputPfxPassword);
    // adicionar caminho do arquivo de entrada com campo de assinatura vazio
    opt.AddInput(new FileDataSource(inputPath));
    // definir caminho do arquivo de saída
    opt.AddOutput(new FileDataSource(outputPath));
    // definir nome do campo de assinatura existente
    opt.Name = "Signature1";
    // executar o processo
    plugin.Process(opt);
```
## O que há de novo no Aspose.PDF 24.3

A partir desta versão foi adicionado o plugin PDF/A Converter para .NET:

```cs
    var options = new PdfAConvertOptions
    {
        PdfAVersion = PdfAStandardVersion.PDF_A_3B
    };

    // Adicione o arquivo fonte
    options.AddInput(new FileDataSource("caminho_para_seu_arquivo_pdf.pdf")); // substitua pelo caminho real do seu arquivo

    // Adicione o caminho para salvar o arquivo convertido
    options.AddOutput(new FileDataSource("caminho_para_o_arquivo_convertido.pdf"));

    // Crie a instância do plugin
    var plugin = new PdfAConverter();

    // Execute a conversão
    plugin.Process(options);
```

- Implementar uma busca por uma lista de frases em um TextFragmentAbsorber:

```cs
    var regexes = new Regex[]
    {
    new Regex(@"(?s)documento\s+(?:(?:no\(?s?\)?\.?)|(?:número(?:\(?s\)?)?))\s+(?:(?:[\w-]*\d[\w-]*)+(?:[,;\s]|e)*)+", RegexOptions.IgnoreCase),
    new Regex(@"[\s\r\n]+Trato[\s\r\n]+de:?", RegexOptions.IgnoreCase),
    new Regex(@"concedido[\s\r\n]+a", RegexOptions.IgnoreCase),
    new Regex("Concedido a:", RegexOptions.IgnoreCase),
    new Regex(@"arquivo.?[\s\r\n]+(?:nos?|números?|#s?|nums?).?[\s\r\n]+(\d+)-(\d+)", RegexOptions.IgnoreCase),
    new Regex(@"arquivo.?[\s\r\n]+nos?.?:?[\s\r\n]+([\d\r\n-]+)", RegexOptions.IgnoreCase)
    };
    var document = new Document(input);
    var absorber = new TextFragmentAbsorber(
    regexes,
    new TextSearchOptions(true)
    );
    document.Pages.Accept(absorber);
    // Obter resultado
    var result = absorber.RegexResults
```
Desde a versão 24.3 é possível adicionar um campo de assinatura vazio em cada página do arquivo PDF/A

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
            // O novo código sugerido, usando o objeto SignatureField (este código funciona bem)
            var doc = new Document(fs);
            var f = new SignatureField(doc.Pages[page], new Rectangle(10, 10, 100, 100));
            // Adiciona a aparência padrão para o campo de assinatura
            f.DefaultAppearance = new DefaultAppearance("Helv", 12, System.Drawing.Color.Black);
            var newAddedField = doc.Form.Add(f, fieldName, page);

            // Como agora fazer newAddedField visível em todas as páginas?
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
## O que há de novo no Aspose.PDF 24.2

Desde 24.2 é possível obter os dados vetoriais de um arquivo PDF

Foi implementado o GraphicsAbsorber para obter dados vetoriais de documentos:

```cs
var doc = new Document(input);
var grAbsorber = new GraphicsAbsorber();
grAbsorber.Visit(doc.Pages[1]);
var elements = grAbsorber.Elements;
var operators = elements[1].Operators;
var rectangle = elements[1].Rectangle;
var position = elements[1].Position;
```

## O que há de novo no Aspose.PDF 24.1

Desde o lançamento 24.1 é possível importar anotações no formato FDF para PDF:

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

Também suporta acesso ao Dicionário da Página ou Catálogo de Documentos.
Também suporta acesso ao Dicionário da Página ou ao Catálogo de Documentos.

Aqui estão exemplos de código para DictionaryEditor:

- Adicionar novos valores

```cs

    // exemplo de nomes de chaves
    string KEY_NAME = "name";
    string KEY_STRING = "str";
    string KEY_BOOL = "bool";
    string KEY_NUMBER = "number";

    var outputPath = "page_dictionary_editor.pdf";
    usando(var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);

        dictionaryEditor.Add(KEY_NAME, new CosPdfName("dados do nome"));
        dictionaryEditor.Add(KEY_STRING, new CosPdfString("dados da string"));
        dictionaryEditor.Add(KEY_BOOL, new CosPdfBoolean(true));
        dictionaryEditor.Add(KEY_NUMBER, new CosPdfNumber(11.2));

        doc.Save(outputPath);
    }
```

- Adicionar e definir valores para o dicionário

```cs

    usando(var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName("Nome antigo"));
        // ou 
        dictionaryEditor[KEY_NAME] = new CosPdfName("Novo nome");
    }
```
- Obter valor do dicionário

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor[KEY_NAME] = new CosPdfName("name");
        var value = dictionaryEditor[KEY_NAME];
        // ou 
        ICosPdfPrimitive primitive;
        dictionaryEditor.TryGetValue(KEY_NAME, out primitive);
    }
```

- Remover valor do dicionário

```cs
    using (var doc = new Document())
    {
        var page = doc.Pages.Add();
        var dictionaryEditor = new DictionaryEditor(page);
        dictionaryEditor.Add(KEY_NAME, new CosPdfName(EXPECTED_NAME));
        dictionaryEditor.Remove(KEY_NAME);
    }
```

## O que há de novo no Aspose.PDF 23.12

O formulário pode ser encontrado e o texto pode ser substituído usando o seguinte trecho de código:

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

Ou, o formulário pode ser completamente removido:

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

Outra variante de remover o formulário:

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

- Todos os formulários podem ser excluídos usando o seguinte trecho de código:

```cs
    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```
- Implementar a conversão de PDF para Markdown:

```cs
    string markdownOutputFilePath = "output.md"
    string inputPdfPath = "input.pdf"
    usando (Document doc = new Document(inputPdfPath))
    {
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.ResourcesDirectoryName = "images"; 
    doc.Save(markdownOutputFilePath, saveOptions);
    }
```

- Implementar a conversão de OFD para PDF:

```cs
    var document = new Document("sample.ofd", new OfdLoadOptions());
    document.Save("sample.pdf");
```

A partir desta versão foi adicionado o plugin Merger:

```cs
    // Caminho para o arquivo PDF mesclado de saída.
    var outputPath = "TestMerge.pdf";

    // Crie uma nova instância de Merger.
    var merger = new Merger();

    // Crie MergeOptions.
    var opt = new MergeOptions();
    opt.AddInput(new FileDataSource(inputPath1));
    opt.AddInput(new FileDataSource(inputPath2));
    opt.AddOutput(new FileDataSource(outputPath));

    // Processar a mesclagem do PDF.
    merger.Process(opt);
```

Também, a partir desta versão foi adicionado o plugin ChatGPT:
Também, a partir desta versão foi adicionado o plugin ChatGPT:

```cs
    using (var plugin = new PdfChatGpt())
    {
    var options = new PdfChatGptRequestOptions();
    options.AddOutput(new FileDataSource("PdfChatGPT_output.pdf")); // Adicione o caminho do arquivo de saída.
    options.ApiKey = "Sua chave de API."; // Você precisa fornecer a chave para acessar a API.
    options.MaxTokens = 1000; // O número máximo de tokens para gerar na conclusão do chat.

    // Adicione as mensagens de solicitação.
    options.Messages.Add(new Message
    {
        Content = "Você é um assistente útil.",
        Role = Role.System
    });
    options.Messages.Add(new Message
    {
        Content = "Qual é o maior diâmetro de pizza já feito?",
        Role = Role.User
    });

    // Processar a solicitação.
    var result = await plugin.ProcessAsync(options);

    var fileResultPath = result.ResultCollection[0].Data;
    var chatCompletionObject = result.ResultCollection[1].Data as ChatCompletion; // O objeto de conclusão do chat da API ChatGPT.
    }
```

## O que há de novo no Aspose.PDF 23.11
## O que há de novo no Aspose.PDF 23.11

A partir desta versão é possível remover texto oculto de arquivos PDF:

```cs
    var document = new Document(inputFile);
    var textAbsorber = new TextFragmentAbsorber();

        // Esta opção pode ser usada para evitar que outros fragmentos de texto se movam após a substituição do texto oculto.
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

Desde o 23.11 suporta interrupção de thread:

```cs

    public void InterruptExample()
    {
        string outputFile = testdata + "sample.pdf";
        //este é um texto grande, usou Lorem Ipsum em 8350 caracteres para causar suspensão 
        string text = ExampleApp.LongText;
        using (InterruptMonitor monitor = new InterruptMonitor())
        {
            RowSpanWorker worker = new RowSpanWorker (outputFile, monitor);
            Thread thread = new Thread(new ThreadStart(worker.Work));
            thread.Start();

            // O tempo limite deve ser menor que o tempo necessário para salvar o documento completo (sem interrupção).
            Thread.Sleep(500);

            // Interromper o processo
            monitor.Interrupt();

            // Aguardar pela interrupção...
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

                    // adicionar uma célula que abrange duas linhas e contém um texto muito longo
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

## Novidades no Aspose.PDF 23.10

A atualização atual apresenta três versões para Remover tags de PDFs marcados.

- Remover algum elemento de nó de um documentElement (elemento raiz da árvore):

```cs
    var document = new Document("algum pdf marcado");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    var structElement = documentElement.Children.Count > 1 ? documentElement.Children[1] as StructElement : null;
    if (documentElement.Children.Remove(structElement))
    {
        // elemento removido
        document.Save(outputPath);
    }

    // Você também pode deletar o structElement em si
    //if (structElement != null)
    //{
    //    structElement.Remove();
    //    document.Save(outputPath);
    //}
```

- Remover todas as tags de elementos marcados do documento, mas manter os elementos da estrutura:

```cs
    var document = new Document("algum pdf marcado");
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
- Remover todas as tags:

```cs
    var document = new Document("some tagged pdf");
    var structure = document.LogicalStructure;
    var documentElement = structure.Children[0];
    documentElement.Remove();
    document.Save(outputPath);
```

Desde 23.10 foi implementada uma nova funcionalidade para medir a altura dos caracteres. Use o seguinte código para medir a altura de um caractere.

```cs
    var doc = new Document(input);
    var absorber = new TextFragmentAbsorber();
    absorber.Visit(doc.Pages[1]);
    var height = absorber.TextFragments[1].TextState.MeasureHeight('A')
```

Observe que a medição é baseada na fonte incorporada no documento. Se faltar alguma informação para uma dimensão, este método retorna 0.

Também, esta versão fornece a funcionalidade de Assinar um PDF usando um HASH assinado:

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
Mais uma nova funcionalidade é a Escala de Página nos Predefinições de Diálogo de Impressão:

```cs
    Document document = new Document();
    document.Pages.Add();
    document.PrintScaling = PrintScaling.None;
    document.Save("output.pdf");
```

## O que há de novo no Aspose.PDF 23.9

Desde o 23.9 suporte para remover uma anotação filha de um campo preenchível.

```cs

    doc = new Document("field-ref-add.pdf");
    field = (Field)doc.Form[fieldName];
    var annotation = field[1];
    doc.Pages[annotation.PageIndex].Annotations.Remove(annotation);
    doc.Save("field-ref-delete.pdf");
```

## O que há de novo no Aspose.PDF 23.8

Desde o 23.8 suporte para adicionar detecção de Atualizações Incrementais.

A função para detectar Atualizações Incrementais em um documento PDF foi adicionada. Esta função retorna 'true' se um documento foi salvo com atualizações incrementais; caso contrário, retorna 'false'.

```cs

    var path = "C:\\test.pdf";
    var doc = new Document(path);
    Console.WriteLine(doc.HasIncrementalUpdate());
```

Além disso, o 23.8 suporta as maneiras de trabalhar com campos de caixas de seleção aninhados.
Também, a versão 23.8 suporta maneiras de trabalhar com campos de caixa de seleção aninhados.

- Criar campo de caixa de seleção com múltiplos valores:

```cs
    using (var document = new Document())
    {
    var page = document.Pages.Add();

    var checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

    // Define o valor da primeira opção do grupo de caixa de seleção
    checkbox.ExportValue = "opção 1";

    // Adiciona uma nova opção diretamente abaixo das existentes
    checkbox.AddOption("opção 2");

    // Adiciona uma nova opção no retângulo especificado
    checkbox.AddOption("opção 3", new Rectangle(100, 100, 120, 120));

    document.Form.Add(checkbox);

    // Seleciona a caixa de seleção adicionada
    checkbox.Value = "opção 2";
    document.Save("checkbox_group.pdf");
    }
```

- Obter e definir o valor de uma caixa de seleção com múltiplos valores:

```cs
    using (Document doc = new Document("example.pdf"))
    {
    Form form = doc.Form;
    CheckboxField checkbox = form.Fields[0] as CheckboxField;

    // Os valores permitidos podem ser recuperados da coleção AllowedStates
    // Define o valor da caixa de seleção usando a propriedade Value
    checkbox.Value = checkbox.AllowedStates[0];
    checkboxValue = checkbox.Value; // o valor definido anteriormente, por exemplo, "opção 1"

    // O valor deve ser qualquer elemento de AllowedStates
    checkbox.Value = "opção 2";
    checkboxValue = checkbox.Value; // opção 2

    // Desmarcar caixas definindo Value como "Off" ou Checked como false
    checkbox.Value = "Off";
    // ou, alternativamente:
    // checkbox.Checked = false;
    checkboxValue = checkbox.Value; // Off
    }
```
## O que há de novo no Aspose.PDF 23.7

Desde o Aspose.PDF 23.7 suporte para adicionar a extração de forma:

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

Também suporta a capacidade de detectar Overflow ao adicionar texto:

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
## O que há de novo no Aspose.PDF 23.6

Do Aspose.PDF 23.6 suporte para adicionar os próximos plugins:

- Aspose PdfConverter Html para PDF
- Aspose PdfOrganizer Redimensionar API
- Aspose PdfOrganizer Comprimir API

Atualize o Aspose.PdfForm 
- adicione o recurso ‘Exportar "Valores" dos campos no documento para arquivo CSV'
- adicione a capacidade de definir propriedades para campos separados

Também suporta a adição da capacidade de definir o título da página HTML, Epub:

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
        Title = "Título para a página"   // <-- isso foi adicionado
    };

    document.Save(Params.OutputPath + "53357-out.html", htmlSaveOptions);
```

## O que há de novo no Aspose.PDF 23.5

Desde a versão 23.5, suporte adicionado para a opção FontSize em RedactionAnnotation. Use o seguinte trecho de código para resolver esta tarefa:

```cs
    Document doc = new Document(dataDir + "test_factuur.pdf");

    // Cria uma instância de RedactionAnnotation para uma região específica da página
    RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(367, 756.919982910156, 420, 823.919982910156));
    annot.FillColor = Aspose.Pdf.Color.Black;

    annot.BorderColor = Aspose.Pdf.Color.Yellow;
    annot.Color = Aspose.Pdf.Color.Blue;
    // Texto a ser impresso na anotação de redação
    annot.OverlayText = "(Desconhecido)";
    annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
    // Repete o texto de sobreposição sobre a anotação de redação
    annot.Repeat = false;
    // Nova propriedade aqui!
    annot.FontSize = 20;
    // Adiciona a anotação à coleção de anotações da primeira página
    doc.Pages[1].Annotations.Add(annot);
    // Aplana a anotação e redige o conteúdo da página (ou seja, remove texto e imagem
    // Sob a anotação redigida)
    annot.Redact();
    dataDir = dataDir + "47704_RedactPage_out_NETCORE.pdf";
    doc.Save(dataDir);
```
## O que há de novo no Aspose.PDF 23.4

Aspose.PDF anunciou o lançamento do SDK .NET 7.

## O que há de novo no Aspose.PDF 23.3.1

A partir do Aspose.PDF 23.3 suporte para adicionar os próximos plugins:

- Aspose.PdfForm
- Aspose.PdfConverter PDF para HTML
- Aspose.PdfConverter PDF para XLSX
- Aspose.PdfOrganizer Rotate
- Aspose.PdfExtrator para Imagens

## O que há de novo no Aspose.PDF 23.3

A versão 23.3 introduziu suporte para adicionar uma resolução a uma imagem. Duas métodos podem ser usados para resolver este problema:

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

E a segunda abordagem:

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
A imagem será posicionada com resolução escalada ou você pode definir as propriedades FixedWidth ou FixedHeight em combinação com IsApplyResolution

## O que há de novo no Aspose.PDF 23.1.1

A partir do Aspose.PDF 23.1.1 suporte para adicionar os próximos plugins:

- Plugin Aspose.PdfOrganizer
- Plugin Aspose.PdfExtractor

## O que há de novo no Aspose.PDF 23.1

Desde a versão 23.1 suporte para criar anotação PrinterMark.

Marcas de impressora são símbolos gráficos ou texto adicionado a uma página para ajudar o pessoal de produção a identificar componentes de um trabalho de múltiplas placas e manter a saída consistente durante a produção. Exemplos comumente usados na indústria gráfica incluem:

- Alvos de registro para alinhar placas
- Rampas de cinza e barras de cor para medir cores e densidades de tinta
- Marcas de corte mostrando onde o meio de saída deve ser cortado

Vamos mostrar o exemplo da opção com barras de cor para medir cores e densidades de tinta.
Vamos mostrar o exemplo da opção com barras coloridas para medir cores e densidades de tinta.

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
Também suporta a extração de imagens vetoriais. Tente usar o seguinte código para detectar e extrair gráficos vetoriais:

```cs
    var doc = new Document(input);
    try{
        doc.Pages[1].TrySaveVectorGraphics(outputSvg);
    }
    catch(Exception){

    }
```

## O que há de novo no Aspose.PDF 22.12

A partir desta versão, suporta converter PDF para Imagem DICOM

```cs
    Document doc = new Document("source.pdf");
    DicomDevice dicom = new DicomDevice();
    FileStream outStream = new FileStream("out.dicom", FileMode.Create, FileAccess.ReadWrite);
    dicom.Process(doc.Pages[1], outStream);
```    

## O que há de novo no Aspose.PDF 22.09

Desde 22.09 suporta adicionar propriedade para modificar a ordem das rubricas do sujeito (E=, CN=, O=, OU=, ) na assinatura.

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
            //ou
            //DigitalSubjectFormat = new SubjectNameElements[] { SubjectNameElements.OU, SubjectNameElements.S, SubjectNameElements.C }
        };
        fileSign.Sign(1, true, rect, signature);
        fileSign.Save(outputPdf);
    }
```
## O que há de novo no Aspose.PDF 22.6

Desde 22.5 suporte para extrair texto SubScript e SuperScript de PDF.

Se o documento PDF contém texto SubScript e SuperScript como H2O, então a extração do texto do PDF também deve extrair suas informações de formatação (no texto plano extraído).
Se o PDF contém texto em itálico, ele também deve ser incluído no conteúdo extraído.

```cs
Document doc = new Document(input);
TextFragmentAbsorber absorber = new TextFragmentAbsorber("TM");
absorber.Visit(doc.Pages[1]);
```

## O que há de novo no Aspose.PDF 22.4

Este lançamento inclui informações para Aspose.PDF para .NET:

- PDF para ODS: Reconhecer texto em subscrito e sobrescrito;

**exemplo**

```cs
Document pdfDocument = new Document("Superscript-Subscript.pdf");
ExcelSaveOptions options = new ExcelSaveOptions();
options.Format = ExcelSaveOptions.ExcelFormat.ODS;
pdfDocument.Save("output.ods", options);
```

- PDF para XMLSpreadSheet2003: Reconhecer texto em subscrito e sobrescrito;

- PDF para Excel: Reconhecer texto em subscrito e sobrescrito;
- PDF para Excel: Reconhecer texto em subscrito e sobrescrito;

- Remover assinaturas UR ao salvar o documento;

- Remover a bandeira Suspects em MarkInfo ao salvar o documento;

- Remover Informações ao salvar o documento

## O que há de novo no Aspose.PDF 22.3

Este lançamento inclui as seguintes atualizações:

- Suporte para AFRelationship;

- Validação de cabeçalho PDF;

- Remover subfiltro adbe.x509.rsa_sha1 ao salvar o documento;

- Formatar campo como Número e Formato de Data;

- Proibir criptografia RC4 no FDF 2.0.

## O que há de novo no Aspose.PDF 22.2

A partir da versão 22.2, é possível assinar um documento usando PdfFileSignature com LTV, e com a possibilidade de alterar o hashing de SHA1 para SHA256.

```csharp
Exemplo de uso:
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
## O que há de novo no Aspose.PDF 22.1

Agora, o Aspose.PDF para .NET suporta o carregamento de documentos de um dos formatos de documento mais populares, Formato de Documento Portátil (PDF) versão 2.0.

## O que há de novo no Aspose.PDF 21.11

### Permitir caracteres não latinos em senha

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

## O que há de novo no Aspose.PDF 21.10

### Como detectar texto oculto?

Por favor, use TextState.Invisible para obter informações sobre a invisibilidade do texto fora da configuração do modo de renderização.

Usamos o seguinte código para testar:

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
    Console.WriteLine("Fragmento {0} em {1}", i, fragment.Rectangle.ToString());
    Console.WriteLine("Texto: {0}", fragment.Text);
    Console.WriteLine("Modo de Renderização: {0}", fragment.TextState.RenderingMode.ToString());
    Console.WriteLine("Invisibilidade: {0}", fragment.TextState.Invisible);
    Console.WriteLine("---");
}
```
### Como obter informações sobre o número de camadas em um documento PDF?

```csharp
Por favor, use o trecho de código:
var inFile = "1234.pdf";
Document doc = new Document(inFile);
List layers = doc.Pages[1].Layers;
```

## O que há de novo no Aspose.PDF 21.9

Personalize a cor de fundo para a aparência da assinatura e a cor da fonte das etiquetas na área de assinatura com Aspose.PDF para .NET.

```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    var rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    var pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//definir cores
        ForegroundColor = Color.DarkGreen,
        BackgroundColor = Color.LightSeaGreen,
    };
    pdfSign.Sign(1, true, rect, pkcs);
    pdfSign.Save(outFile);
}
```

## O que há de novo no Aspose.PDF 21.8

### Como alterar a cor do texto em Assinatura Digital?

Na versão 21.8, a propriedade ForegroundColor permite alterar a cor do texto em Assinatura Digital.

```csharp
```csharp
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(inFile);
    //criar um retângulo para localização da assinatura
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);
    PKCS7 pkcs = new PKCS7(inPfxFile, "");
    pkcs.CustomAppearance = new SignatureCustomAppearance()
    {//definir cor do texto
        ForegroundColor = Color.Green
    };
    // assinar o arquivo PDF
    pdfSign.Sign(1, true, rect, pkcs);
    //salvar arquivo PDF de saída
    pdfSign.Save(outFile);
}
```

## Novidades no Aspose.PDF 21.7

### Criação de PDF baseado em XML e XLS com parâmetros

Para adicionar parâmetros XSL, precisamos criar nossa própria [XsltArgumentList](https://docs.microsoft.com/en-us/dotnet/api/system.xml.xsl.xsltargumentlist?view=net-5.0) e definir como propriedade em [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). O trecho a seguir mostra como usar essa classe com os arquivos de exemplo descritos acima.

```csharp
public static void Example_XSLFO_to_PDF()
    {
        var XmlContent = File.ReadAllText(_dataDir + "employees.xml");
        var XsltContent = File.ReadAllText(_dataDir + "employees.xslt");

        var options = new Aspose.Pdf.XslFoLoadOptions();

        //Exemplo de uso de XsltArgumentList
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
## O que há de novo no Aspose.PDF 21.6

Com o Aspose.PDF para .NET você pode ocultar imagens usando ImagePlacementAbsorber do documento:

```csharp
public void PDFNET_49961()
{
   ImagePlacementAbsorber abs = new ImagePlacementAbsorber();
   Document doc = new Document("test.pdf");
   // Ocultar imagem na primeira página
   doc.Pages[1].Accept(abs);

   foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
   {
       imagePlacement.Hide();
   }

   doc.Save("test_out.pdf");
}
```

## O que há de novo no Aspose.PDF 21.5

### Como extrair o nome completo da fonte a partir da sua descrição/recurso no PDF?

Você pode obter uma fonte completa com o prefixo com a propriedade BaseFont para a classe Font.

```csharp
Document pdf = new Document(dataDir + @"testfont.pdf");

Aspose.Pdf.Text.Font[] fonts = pdf.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine($"font name : {font.FontName} BaseFont name : {font.BaseFont}");
}
pdf.Dispose();
```

## O que há de novo no Aspose.PDF 21.4

### Adicionar API para mesclar imagens

O Aspose.PDF 21.4 permite que você combine imagens.
Aspose.PDF 21.4 permite que você combine Imagens.

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

## Novidades no Aspose.PDF 21.3

### Exposição pública da propriedade para detectar a Proteção de Informações Azure
### Exposição pública de propriedade para detectar a Proteção de Informações do Azure

Com o próximo trecho de código, você deverá ser capaz de acessar o conteúdo criptografado de seus arquivos PDF, protegidos com a Proteção de Informações do Azure:

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

## O que há de novo no Aspose.PDF 21.1

### Adição de suporte para recuperar a cor de fundo do TextFragment

Nesta versão do Aspose.PDF, a função tornou-se disponível para recuperar a cor de fundo.
Nesta versão do Aspose.PDF, a função ficou disponível para recuperar a cor de fundo.

Considere o seguinte código:

```csharp
Document pdfDocument = new Document(dataDir + "TextColor.pdf");
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber();

TextSearchOptions searchOptions = new TextSearchOptions(false);
searchOptions.SearchForTextRelatedGraphics = true;

textFragmentAbsorber.TextSearchOptions = searchOptions;

// Aceita o absorvedor para todas as páginas
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Obtém os fragmentos de texto extraídos
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Percorre os fragmentos
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Texto: '{0}'", textFragment.Text);
    Console.WriteLine("Cor de Fundo: '{0}'", textFragment.TextState.BackgroundColor);
    Console.WriteLine("Cor de Primeiro Plano: '{0}'", textFragment.TextState.ForegroundColor);
    Console.WriteLine("Cor de Fundo do Segmento: '{0}'", textFragment.Segments[1].TextState.BackgroundColor);
}
```
### Após a conversão para HTML, a fonte é totalmente incorporada no resultado

Também no Aspose.PDF 21.1, após converter PDF para HTML, tornou-se disponível fontes incorporadas em um documento HTML de saída. Isso é possível com a nova opção booleana de salvar HtmlSaveParameter.SaveFullFont.

Aqui está o trecho de código:

```csharp
HtmlSaveOptions saveOptions = new HtmlSaveOptions();
saveOptions.RasterImagesSavingMode = HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground;
saveOptions.PartsEmbeddingMode = HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml;
saveOptions.LettersPositioningMethod = HtmlSaveOptions.LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss;
saveOptions.FontSavingMode = HtmlSaveOptions.FontSavingModes.AlwaysSaveAsTTF;
saveOptions.SaveTransparentTexts = true;
saveOptions.SaveFullFont = true;
```
