---
title: Licenciamento e limitações
linktitle: Licenciamento e limitações
type: docs
weight: 50
url: /pt/androidjava/licensing/
description: Aspose.PDF for Android via Java convida seus clientes a obter uma Classic license e uma Metered License. Também pode usar uma licença limitada para explorar melhor o produto.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes minuciosamente antes de comprar, por isso a versão de avaliação permite que você a use como normalmente faria.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF for Android via Java fornece funcionalidade completa do produto, mas todas as páginas nos documentos PDF gerados são marcadas com a marca d'água "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

- **O limite do número de itens de coleção que podem ser processados.**
Na versão de avaliação de qualquer coleção, você pode processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).

Você pode baixar uma versão de avaliação do Aspose.PDF for Android via Java de [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). A versão de avaliação fornece exatamente as mesmas capacidades que a versão licenciada do produto. Além disso, a versão de avaliação simplesmente se torna licenciada quando você compra uma licença e adiciona algumas linhas de código para aplicar a licença.

Uma vez que você esteja satisfeito com sua avaliação do **Aspose.PDF**, você pode [adquirir uma licença](https://purchase.aspose.com/) no site da Aspose. Familiarize-se com os diferentes tipos de assinatura oferecidos. Se você tiver alguma dúvida, não hesite em contatar a equipe de vendas da Aspose.

Cada licença da Aspose inclui uma assinatura de um ano para atualizações gratuitas a quaisquer novas versões ou correções que sejam lançadas durante esse período. O suporte técnico é gratuito e ilimitado, e é fornecido tanto para usuários licenciados quanto para usuários de avaliação.

>Se você quiser testar o Aspose.PDF for Android via Java sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, como mostrado no exemplo abaixo.

A licença é um arquivo XML de texto simples que contém detalhes como o nome do produto, o número de desenvolvedores aos quais está licenciada, a data de expiração da assinatura etc. O arquivo é assinado digitalmente, portanto não o modifique; até mesmo a adição inadvertida de uma quebra de linha extra no arquivo o invalidará.

É necessário definir uma licença antes de executar qualquer operação com documentos. Você só precisa definir a licença uma vez por aplicação ou processo.

A licença pode ser carregada a partir de um stream ou arquivo nos seguintes locais:

1. Caminho explícito.
1. A pasta que contém o aspose-pdf-xx.x.jar.

Use o método License.setLicense para licenciar o componente. Muitas vezes, a maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o Aspose.PDF.jar e especificar apenas o nome do arquivo sem caminho, como mostrado no exemplo a seguir:

{{% alert color="primary" %}}

A partir do Aspose.PDF for Java 4.2.0, você precisa chamar as linhas de código a seguir para inicializar a licença.

{{% /alert %}}

### Carregando uma licença de um arquivo

Neste exemplo, **Aspose.PDF** tentará encontrar o arquivo de licença na pasta que contém os JARs da sua aplicação.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Carregando a licença a partir de um objeto stream

O exemplo a seguir mostra como carregar uma licença a partir de um stream.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Configurando uma Licença Adquirida Antes de 2005/01/22

**Aspose.PDF** para Java não suporta mais licenças antigas, então, por favor, entre em contato com o nosso [equipe de vendas](https://company.aspose.com/contact) para obter um novo arquivo de licença.

### Validar a Licença

É possível validar se a licença foi definida corretamente ou não. A classe Document possui o método isLicensed que retornará true se a licença foi definida corretamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Licença Medida

Aspose.PDF permite que os desenvolvedores apliquem chave de medição. É um novo mecanismo de licenciamento. O novo mecanismo de licenciamento será usado juntamente com o método de licenciamento existente. Os clientes que desejam ser cobrados com base no uso dos recursos da API podem usar o licenciamento por medição. Para mais detalhes, consulte [FAQ de Licença por Medição](https://purchase.aspose.com/faqs/licensing/metered) seção.

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
## Usando Vários Produtos da Aspose

Se você usar vários produtos Aspose em sua aplicação, por exemplo Aspose.PDF e Aspose.Words, aqui estão algumas dicas úteis.

- **Defina a Licença para cada Produto Aspose Separadamente.** Mesmo que você possua um único arquivo de licença para todos os componentes, por exemplo 'Aspose.Total.lic', ainda é necessário chamar **License.SetLicense** separadamente para cada produto Aspose que você está usando em sua aplicação.
- **Use o Nome de Classe de Licença totalmente Qualificado.** Cada produto Aspose possui uma classe **License** em seu namespace. Por exemplo, Aspose.PDF tem a classe **com.aspose.pdf.License** e Aspose.Words tem a classe **com.aspose.words.License**. Usar o nome de classe totalmente qualificado permite evitar qualquer confusão sobre qual licença é aplicada a qual produto.

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
