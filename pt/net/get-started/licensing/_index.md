---
title: Aspose PDF License
linktitle: Licenciamento e limitações
type: docs
weight: 90
url: /pt/net/licensing/
description: Aspose. PDF para .NET convida seus clientes a obter uma licença Clássica e Licença Medida. Bem como usar uma licença limitada para explorar melhor o produto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes completamente antes de comprar, então a versão de avaliação permite que você a use como faria normalmente.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF para .NET oferece total funcionalidade do produto, mas todas as páginas nos documentos PDF gerados são marcadas com "Avaliação Apenas. Criado com Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

- **Limite do número de itens de coleção que podem ser processados.**
Na versão de avaliação de qualquer coleção, você pode processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).
Na versão de avaliação de qualquer coleção, você pode processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).

>Se você deseja testar o Aspose.HTML para .NET sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada a partir de um arquivo ou objeto de fluxo. A maneira mais fácil de configurar uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, conforme mostrado no exemplo abaixo.

Se você usar qualquer outro componente Aspose para .NET junto com o Aspose.PDF para .NET, por favor, especifique o namespace para License como [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Carregando uma licença de arquivo

A maneira mais fácil de aplicar uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar apenas o nome do arquivo sem um caminho.

Quando você chama o método [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), o nome da licença que você passa deve ser o do seu arquivo de licença.
Quando você chama o método [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), o nome da licença que você passa deve ser o do seu arquivo de licença.

```csharp
public static void SetLicenseExample()
{
    // Inicializar objeto de licença
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // Definir licença
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // algo deu errado
        throw;
    }
    Console.WriteLine("Licença definida com sucesso.");
}
```
### Carregando a licença de um objeto stream

O exemplo a seguir mostra como carregar uma licença de um stream.

```csharp
public static void SetLicenseFromStream()
{
    // Inicializar objeto de licença
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // Carregar licença do stream do arquivo
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Definir licença
    license.SetLicense(myStream);
    Console.WriteLine("Licença definida com sucesso.");
}
```
## Licença Medida

Aspose.PDF permite aos desenvolvedores aplicar chave medida. É um novo mecanismo de licenciamento. O novo mecanismo de licenciamento será usado juntamente com o método de licenciamento existente. Aqueles clientes que desejam ser cobrados com base no uso das funcionalidades da API podem usar o licenciamento medido. Para mais detalhes, consulte a seção de Perguntas Frequentes sobre Licenciamento Medido.

Uma nova classe Metered foi introduzida para aplicar a chave medida. A seguir está o código de exemplo demonstrando como configurar chaves públicas e privadas medidas.

Para mais detalhes, por favor, consulte a seção de [Perguntas Frequentes sobre Licenciamento Medido](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // definir chaves públicas e privadas medidas
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Acesse a propriedade setMeteredKey e passe chaves públicas e privadas como parâmetros
    metered.SetMeteredKey(
        "<insira a chave pública aqui>",
        "<insira a chave privada aqui>");

    // Carregar o documento do disco.
    Document doc = new Document("input.pdf");
    //Obter a contagem de páginas do documento
    Console.WriteLine(doc.Pages.Count);
}
```
Por favor, note que aplicações COM que trabalham com **Aspose.PDF for .NET** também devem usar a classe License.

Um ponto que precisa de consideração:
Por favor, note que os recursos incorporados são incluídos no assembly da maneira como são adicionados, ou seja, se você adicionar um arquivo de texto como um recurso incorporado na aplicação e abrir o EXE resultante no bloco de notas, você verá o conteúdo exato do arquivo de texto. Portanto, ao usar o arquivo de licença como um recurso incorporado, qualquer pessoa pode abrir o arquivo exe em algum editor de texto simples e ver/extrair o conteúdo da licença incorporada.

Portanto, para adicionar uma camada extra de segurança ao incorporar a licença com a aplicação, você pode comprimir/criptografar a licença e, depois disso, incorporá-la ao assembly. Suponha que temos o arquivo de licença Aspose.PDF.lic, então vamos criar Aspose.PDF.zip com a senha test e incorporar este arquivo zip na solução. O seguinte trecho de código pode ser usado para inicializar a licença:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Obter a contagem de páginas do documento
            Console.WriteLine(doc.Pages.Count);
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
    }
}
```
### Aplicando uma Licença Comprada Antes de 22/01/2005

Aspose.PDF para .NET não suporta mais as licenças antigas. Se você possui uma licença de antes de 22 de janeiro de 2005 e atualizou para uma versão mais recente do Aspose.PDF, por favor, entre em contato com nossa equipe de Vendas para obter um novo arquivo de licença.
