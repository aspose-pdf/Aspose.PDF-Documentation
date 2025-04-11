---
title: Licença Aspose PDF
linktitle: Licenciamento e limitações
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /pt/net/licensing/
description: Aspose. PDF para .NET convida seus clientes a obter uma licença Clássica e Licença Medida. Além de usar uma licença limitada para explorar melhor o produto.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF para .NET introduz uma estrutura de licenciamento robusta, incluindo licenças Clássicas e Medidas, permitindo que os usuários escolham entre preços fixos e opções de cobrança baseadas no uso. A licença Clássica pode ser facilmente carregada de um arquivo ou fluxo, enquanto a inovadora licença Medida fornece medição flexível com base no uso da API, atendendo a diversas necessidades dos usuários. Essa estratégia de licenciamento dual melhora a acessibilidade e escalabilidade das soluções PDF para desenvolvedores.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes minuciosamente antes de comprar, então a versão de avaliação permite que você a use como normalmente faria.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação de Aspose.PDF for .NET fornece funcionalidade total do produto, mas todas as páginas nos documentos PDF gerados estão marcadas com o texto "Avaliação Apenas. Criado com Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." na parte superior.

- **Limitar o número de páginas que podem ser processadas.**
Na versão de avaliação, você pode processar apenas as quatro primeiras páginas de um documento.

>Se você deseja testar Aspose.PDF for .NET sem as limitações da versão de avaliação, você também pode solicitar uma Licença Temporária de 30 dias. Consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença Clássica

A licença pode ser carregada de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, como mostrado no exemplo abaixo.

Se você usar qualquer outro componente Aspose para .NET junto com Aspose.PDF for .NET, por favor, especifique o namespace para Licença como [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Carregando uma licença de um arquivo

A maneira mais fácil de aplicar uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar apenas o nome do arquivo sem um caminho.

Quando você chama o método [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), o nome da licença que você passa deve ser o do seu arquivo de licença. Por exemplo, se você mudar o nome do arquivo de licença para "Aspose.PDF.lic.xml", passe esse nome de arquivo para o método Pdf.SetLicense(…).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Carregando a licença de um objeto de fluxo

O seguinte exemplo mostra como carregar uma licença de um fluxo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Licença Medida

Aspose.PDF permite que os desenvolvedores apliquem uma chave medida. O mecanismo de licenciamento medido será usado juntamente com o método de licenciamento existente. Aqueles clientes que desejam ser cobrados com base no uso dos recursos da API podem usar o licenciamento medido. Para mais detalhes, consulte a seção FAQ de Licenciamento Medido.
Este guia fornece as melhores práticas para uma implementação suave e para evitar interrupções devido a mudanças no status da licença.

A classe "Medida" é usada para aplicar chaves medidas. A seguir está o código de exemplo que demonstra como definir chaves públicas e privadas medidas.

Para mais detalhes, consulte a seção [FAQ de Licenciamento Medido](https://purchase.aspose.com/faqs/licensing/metered).

__Métodos de Licenciamento Medido__

Aplicando a Licença Medida, use o método `SetMeteredKey` para ativar a licença medida fornecendo suas chaves públicas e privadas. Isso deve ser feito uma vez durante a inicialização do aplicativo para garantir o licenciamento adequado.

Exemplo:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Verificando o Status da Licença usa `IsMeteredLicensed()` para verificar se a licença medida está ativa.

Exemplo:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
O método `Metered.GetConsumptionCredit()` é usado para obter informações sobre créditos de consumo.
O método `Metered.GetConsumptionQuantity()` é usado para obter informações sobre o tamanho do arquivo de consumo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");
    // Get current Consumption Credit and Quantity
    var currentMonthCreditsSpent = Aspose.Pdf.Metered.GetConsumptionCredit();
    var currentMonthConsumedMegabytes = Aspose.Pdf.Metered.GetConsumptionQuantity();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Add five pages
        AddPages(document, 5);

        // Save the document
        document.Save(dataDir + "output.pdf");

        // Wait to be sure the transaction completed
        System.Threading.Thread.Sleep(10000);
        // Get current Consumption Credit and Quantity
        var nowCredit = Aspose.Pdf.Metered.GetConsumptionCredit();
        var nowQuantity = Aspose.Pdf.Metered.GetConsumptionQuantity();
        Console.WriteLine("Credit: was={0} now={1} difference={2}", currentMonthCreditsSpent, nowCredit, nowCredit - currentMonthCreditsSpent);
        Console.WriteLine("Quantity: was={0} now={1} difference={2}", currentMonthConsumedMegabytes, nowQuantity, nowQuantity - currentMonthConsumedMegabytes); 
    }
}

private static void AddPages(Document document, int n)
{
    for (int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}
```

__Melhores Práticas para Licenciamento Medido__

✅ Abordagem Recomendada: Padrão Singleton
Para garantir uma configuração de licenciamento estável:

- Aplique a licença uma vez na inicialização do aplicativo.
- Use um padrão singleton (ou abordagem semelhante) para criar e reutilizar a instância da licença medida.
- Verifique periodicamente o status da licença usando `IsMeteredLicensed()`. Reaplique a licença apenas se ela se tornar inválida.
- Se implementado corretamente, a licença permanece válida por 24 horas, mesmo que o servidor de licença esteja temporariamente indisponível.

Exemplo: Implementação Singleton

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Erros Comuns a Evitar:

- Aplicações Frequentes de Licença
- Não crie uma nova instância de licença medida para cada operação.
- Se o servidor de licença estiver inacessível durante a inicialização, a licença pode reverter para o modo de avaliação.
- Não aplique a licença repetidamente para cada operação.
- Aplicações frequentes de licença podem causar a reversão para o modo de teste se o servidor de licença estiver temporariamente indisponível.

__Resumo:__

✅ Defina a licença medida uma vez na inicialização do aplicativo.
✅ Use um padrão singleton para gerenciar uma única instância.
✅ Verifique periodicamente e reaplique a licença se necessário.
❌ Evite aplicações frequentes de licença para prevenir a reversão para o modo de teste.
Seguindo essas melhores práticas, você garante um uso suave e ininterrupto do Aspose.PDF com licenciamento medido.

Se a licença foi inicializada, então enquanto este objeto "vive", mesmo que a conexão com o servidor de licença seja perdida por algum motivo, a licença será considerada ativa por mais 7 dias. Se você inicializar uma licença sempre que precisar fazer algo e não houver conexão com o servidor no momento da inicialização, então a licença entrará no modo de avaliação.
Deve-se enfatizar adicionalmente que se um usuário inicializou uma licença, então enquanto este objeto "vive", mesmo que a conexão com o servidor de licença seja perdida por algum motivo, a licença será considerada ativa por mais 24 horas. Se você inicializar uma licença sempre que precisar fazer algo e não houver conexão com o servidor no momento da inicialização, então a licença entrará no modo de avaliação.

Observe que aplicativos COM que trabalham com **Aspose.PDF for .NET** também devem usar a classe License.

Um ponto que precisa de consideração:
Observe que os recursos incorporados são incluídos na montagem da maneira como foram adicionados, ou seja, se você adicionar um arquivo de texto como um recurso incorporado no aplicativo e abrir o EXE resultante no bloco de notas, você verá o conteúdo exato do arquivo de texto. Portanto, ao usar o arquivo de licença como um recurso incorporado, qualquer um pode abrir o arquivo exe em algum editor de texto simples e ver/extrair o conteúdo da licença incorporada.

Portanto, para colocar uma camada extra de segurança ao incorporar a licença com o aplicativo, você pode compactar/encriptar a licença e, após isso, pode incorporá-la na montagem. Suponha que temos o arquivo de licença Aspose.PDF.lic, então vamos fazer Aspose.PDF.zip com a senha test e incorporar este arquivo zip na solução. O seguinte trecho de código pode ser usado para inicializar a licença:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
}

private static Stream GetSecureLicenseFromStream()
{
    var assembly = Assembly.GetExecutingAssembly();
    var memoryStream = new MemoryStream();
    using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
    {
        using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
        {
            var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
            unpackedLicense?.Open().CopyTo(memoryStream);
        }
    }

    memoryStream.Position = 0;
    return memoryStream;
}
```