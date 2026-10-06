---
title: Licença Aspose PDF
linktitle: Licenciamento e limitações
type: docs
weight: 50
url: /pt/java/licensing/
description: Aspose.PDF for Python convida seus clientes a obter uma licença Classic. Além disso, use uma licença limitada para explorar melhor o produto.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamento do Aspose.PDF for Java
Abstract: O artigo discute as limitações e opções de licenciamento para Aspose.PDF for Python. Ele destaca que a versão de avaliação permite testar todas as funcionalidades, mas adiciona uma marca d'água aos PDFs gerados, indicando “Evaluation Only” juntamente com informações de direitos autorais. Para usuários que desejam testar sem essas limitações, está disponível uma Licença Temporária de 30 dias. O artigo ainda explica como implementar uma licença clássica carregando-a a partir de um arquivo ou stream, recomendando colocar o arquivo de licença no mesmo diretório do arquivo Aspose.PDF.dll e definir a licença usando a classe `Aspose.Pdf.License`. Trechos de código são fornecidos para ilustrar o processo de licenciamento.
---
## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes minuciosamente antes de comprar, por isso a versão de avaliação permite que você a use como faria normalmente.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF for Java oferece funcionalidade total do produto, mas todas as páginas nos documentos PDF gerados são marcadas com "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

- **O limite do número de itens de coleção que podem ser processados.**
Na versão de avaliação de qualquer coleção, você pode processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).

Você pode baixar uma versão de avaliação do **Aspose.PDF** para Java a partir de [Repositório Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). A versão de avaliação fornece exatamente as mesmas capacidades da versão licenciada do produto. Além disso, a versão de avaliação simplesmente se torna licenciada quando você compra uma licença e adiciona algumas linhas de código para aplicar a licença.

Quando você estiver satisfeito com sua avaliação do **Aspose.PDF**, você pode [adquirir uma licença](https://purchase.aspose.com/) no site da Aspose. Familiarize-se com os diferentes tipos de assinatura oferecidos. Se você tiver alguma dúvida, não hesite em entrar em contato com a equipe de vendas da Aspose.

Cada licença da Aspose inclui uma assinatura de um ano para atualizações gratuitas para quaisquer novas versões ou correções lançadas durante esse período. O suporte técnico é gratuito e ilimitado e é fornecido tanto para usuários licenciados quanto para usuários em avaliação.

>Se você quiser testar o Aspose.PDF for Java sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada a partir de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, como mostrado no exemplo abaixo.

A licença é um arquivo XML de texto simples que contém detalhes como o nome do produto, número de desenvolvedores para os quais está licenciada, data de expiração da assinatura e assim por diante. O arquivo é assinado digitalmente, portanto não o modifique; até mesmo a adição inadvertida de uma quebra de linha extra no arquivo invalida‑o.

É necessário definir uma licença antes de realizar quaisquer operações com documentos. Você só precisa definir a licença uma vez por aplicativo ou processo.

A licença pode ser carregada a partir de um stream ou arquivo nos seguintes locais:

1. Caminho explícito.
1. A pasta que contém o aspose-pdf-xx.x.jar.

Use o método License.setLicense para licenciar o componente. Muitas vezes, a maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o Aspose.PDF.jar e especificar apenas o nome do arquivo sem o caminho, como mostrado no exemplo a seguir:

{{% alert color="primary" %}}

A partir do Aspose.PDF for Java 4.2.0, você precisa chamar as linhas de código a seguir para inicializar a licença.

{{% /alert %}}

### Carregar uma licença a partir de um arquivo

Neste exemplo **Aspose.PDF** tentará encontrar o arquivo de licença na pasta que contém os JARs da sua aplicação.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Carregar uma licença a partir de um fluxo

O exemplo a seguir mostra como carregar uma licença a partir de um stream.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### Validar a licença

É possível validar se a licença foi configurada corretamente ou não. A classe Document tem o método isLicensed que retornará true se a licença foi configurada corretamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## Licenciamento por medição

O licenciamento por medição permite a cobrança com base no uso dos recursos da API. Ele pode ser usado junto com o mecanismo de licenciamento existente. Para obter mais detalhes, consulte as [perguntas frequentes sobre licenciamento por medição](https://purchase.aspose.com/faqs/licensing/metered).

A classe [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) permite configurar as chaves de licenciamento por medição. O exemplo a seguir mostra como definir as chaves pública e privada.

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

## Usar vários produtos da Aspose

Se você usar vários produtos da Aspose em sua aplicação, por exemplo Aspose.PDF e Aspose.Words, aqui estão algumas dicas úteis.

- **Defina a licença de cada produto Aspose separadamente.** Mesmo que você tenha um único arquivo de licença para todos os componentes, por exemplo 'Aspose.Total.lic', ainda é necessário chamar **License.SetLicense** separadamente para cada produto Aspose que você está usando em sua aplicação.
- **Use o nome de classe de licença totalmente qualificado.** Cada produto Aspose possui uma classe **License** em seu namespace. Por exemplo, Aspose.PDF tem a classe **com.aspose.pdf.License** e Aspose.Words tem a classe **com.aspose.words.License**. Usar o nome de classe totalmente qualificado permite evitar qualquer confusão sobre qual licença é aplicada a qual produto.

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
