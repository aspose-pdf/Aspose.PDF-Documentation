---
title: Aspose Licença PDF
linktitle: Licenciamento e limitações
type: docs
weight: 50
url: /java/licensing/
description: Aspose.PDF for Python convida seus clientes a obter uma licença Classic. Além de usar uma licença limitada para explorar melhor o produto.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamento de Aspose.PDF para Java
Abstract: O artigo discute as limitações e opções de licenciamento do Aspose.PDF para Python. Ele destaca que a versão de avaliação permite testes completos de funcionalidade, mas adiciona uma marca d’água aos PDFs gerados, informando “Somente avaliação” junto com informações de direitos autorais. Para usuários que desejam testar sem essas limitações, está disponível uma Licença Temporária de 30 dias. O artigo explica ainda como implementar uma licença clássica carregando-a de um arquivo ou fluxo, recomendando colocar o arquivo de licença no mesmo diretório do arquivo Aspose.PDF.dll e definir a licença usando a classe `Aspose.Pdf.License`. Trechos de código são fornecidos para ilustrar o processo de licenciamento.
---
## Limitação de uma versão de avaliação

Queremos que nossos clientes testem minuciosamente nossos componentes antes de comprar, para que a versão de avaliação permita que você os use normalmente.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF para Java fornece funcionalidade completa do produto, mas todas as páginas nos documentos PDF gerados têm marca d'água com "Apenas avaliação. Criado com Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" na parte superior.

- **O limite do número de itens de coleção que podem ser processados.**
Na versão de avaliação de qualquer coleção, é possível processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).

Você pode baixar uma versão de avaliação do **Aspose.PDF** para Java em [Repositório Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). A versão de avaliação oferece absolutamente os mesmos recursos que a versão licenciada do produto. Além disso, a versão de avaliação simplesmente se torna licenciada quando você compra uma licença e adiciona algumas linhas de código para aplicá-la.

Quando estiver satisfeito com sua avaliação de **Aspose.PDF**, você pode [comprar uma licença](https://purchase.aspose.com/) no site da Aspose. Familiarize-se com os diferentes tipos de assinatura oferecidos. Se você tiver alguma dúvida, não hesite em entrar em contato com a equipe de vendas da Aspose.

Cada licença Aspose traz uma assinatura de um ano para atualizações gratuitas para quaisquer novas versões ou correções lançadas durante esse período. O suporte técnico é gratuito e ilimitado e fornecido tanto para usuários licenciados quanto para avaliação.

>Se quiser testar o Aspose.PDF para Java sem as limitações da versão de avaliação, você também pode solicitar uma licença temporária de 30 dias. Consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta do arquivo Aspose.PDF.dll e especificar o nome do arquivo sem caminho, conforme mostrado no exemplo abaixo.

A licença é um arquivo XML de texto simples que contém detalhes como nome do produto, número de desenvolvedores para os quais está licenciado, data de expiração da assinatura e assim por diante. O arquivo é assinado digitalmente, portanto não modifique o arquivo; mesmo a adição inadvertida de uma quebra de linha extra no arquivo irá invalidá-lo.

Você precisa definir uma licença antes de realizar qualquer operação com documentos. Você só precisa definir uma licença uma vez por aplicativo ou processo.

A licença pode ser carregada de um fluxo ou arquivo nos seguintes locais:

1. Caminho explícito.
1. A pasta que contém aspose-pdf-xx.x.jar.

Use o método License.setLicense para licenciar o componente. Muitas vezes, a maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que Aspose.PDF.jar e especificar apenas o nome do arquivo sem caminho, conforme mostrado no exemplo a seguir:

{{% alert color="primary" %}}

A partir do Aspose.PDF para Java 4.2.0, você precisa chamar as linhas de código a seguir para inicializar a licença.

{{% /alert %}}

### Carregando uma licença do arquivo

Neste exemplo **Aspose.PDF** tentará encontrar o arquivo de licença na pasta que contém os JARs do seu aplicativo.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Carregando a licença de um objeto de fluxo

O exemplo a seguir mostra como carregar uma licença de um stream.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### Validar a licença

É possível validar se a licença foi configurada corretamente ou não. A classe Document possui o método isLicensed que retornará verdadeiro se a licença tiver sido definida corretamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## Licença medida

Aspose.PDF permite que os desenvolvedores apliquem chave medida. É um novo mecanismo de licenciamento. O novo mecanismo de licenciamento será utilizado juntamente com o método de licenciamento existente. Os clientes que desejam ser cobrados com base no uso dos recursos da API podem usar o licenciamento medido. Para obter mais detalhes, consulte [Perguntas frequentes sobre licenciamento medido](https://purchase.aspose.com/faqs/licensing/metered)Seção.

Uma nova classe [Medido](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В foi introduzido para aplicar chave medida. A seguir está o código de exemplo que demonstra como definir chaves públicas e privadas medidas.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```

## Usando vários produtos da Aspose

Se você usa vários produtos Aspose em seu aplicativo, por exemplo Aspose.PDF e Aspose.Words, aqui estão algumas dicas úteis.

- **Defina a licença para cada produto Aspose separadamente.** Mesmo se você tiver um único arquivo de licença para todos os componentes, por exemplo 'Aspose.Total.lic', você ainda precisará chamar **License.SetLicense** separadamente para cada produto Aspose que estiver usando em seu aplicativo.
- **Use o nome da classe de licença totalmente qualificada.** Cada produto Aspose tem uma classe **License** em seu namespace. Por exemplo, Aspose.PDF possui **com.aspose.pdf.License** e Aspose.Words possui a classe **com.aspose.words.License**. Usar o nome de classe totalmente qualificado permite evitar qualquer confusão sobre qual licença é aplicada a qual produto.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
