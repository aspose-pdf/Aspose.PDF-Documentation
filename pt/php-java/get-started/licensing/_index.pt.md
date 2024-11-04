---
title: Licenciamento e limitações
linktitle: Licenciamento e limitações
type: docs
weight: 90
url: /php-java/licensing/
description: Aspose.PDF para PHP via Java convida seus clientes a obter uma licença Clássica e Licença Medida. Assim como usar uma licença limitada para explorar melhor o produto.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes minuciosamente antes de comprar, então a versão de avaliação permite que você a use como faria normalmente.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF para PHP via Java fornece funcionalidade completa do produto, mas todas as páginas nos documentos PDF gerados são marcadas com "Somente Avaliação. Criado com Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

- **O limite do número de itens da coleção que podem ser processados.**

Na versão de avaliação de qualquer coleção, você pode processar apenas quatro elementos (por exemplo, apenas 4 páginas, 4 campos de formulário, etc.).

Você pode baixar uma versão de avaliação do **Aspose.PDF** para Java a partir do [Repositório Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). A versão de avaliação oferece exatamente as mesmas capacidades que a versão licenciada do produto. Além disso, a versão de avaliação simplesmente se torna licenciada quando você compra uma licença e adiciona algumas linhas de código para aplicar a licença.

Uma vez que você esteja satisfeito com sua avaliação do **Aspose.PDF**, você pode [comprar uma licença](https://purchase.aspose.com/) no site da Aspose. Familiarize-se com os diferentes tipos de assinatura oferecidos. Se tiver alguma dúvida, não hesite em contatar a equipe de vendas da Aspose.

Toda licença Aspose inclui uma assinatura de um ano para atualizações gratuitas para quaisquer novas versões ou correções que sejam lançadas durante este período. O suporte técnico é gratuito e ilimitado e é fornecido tanto para usuários licenciados quanto para usuários de avaliação.

>Se você deseja testar o Aspose.PDF para PHP via Java sem as limitações da versão de avaliação, você também pode solicitar uma Licença Temporária de 30 dias.
 Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada a partir de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, como mostrado no exemplo abaixo.

A licença é um arquivo XML de texto simples que contém detalhes como o nome do produto, número de desenvolvedores para os quais está licenciada, data de expiração da assinatura e assim por diante. O arquivo é assinado digitalmente, portanto, não modifique o arquivo; mesmo a adição inadvertida de uma quebra de linha extra no arquivo o invalidará.

Você precisa definir uma licença antes de realizar qualquer operação com documentos. Você só precisa definir uma licença uma vez por aplicação ou processo.

A licença pode ser carregada a partir de um fluxo ou arquivo nos seguintes locais:

1. Caminho explícito.
1. A pasta que contém o aspose-pdf-xx.x.jar.

Use o método License.setLicense para licenciar o componente. Freqüentemente, a maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que Aspose.PDF.jar e especificar apenas o nome do arquivo sem o caminho, como mostrado no exemplo a seguir:

{{% alert color="primary" %}}

A partir do Aspose.PDF para PHP via Java 4.2.0, você precisa chamar as seguintes linhas de código para inicializar a licença.

{{% /alert %}}

### Carregando uma licença a partir de um arquivo

Neste exemplo, o **Aspose.PDF** tentará encontrar o arquivo de licença na pasta que contém os JARs da sua aplicação.

```java
// Inicializar Instância de Licença
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Chamar método setLicense para definir a licença
license.setLicense("Aspose.Pdf.Java.lic");
```
### Carregando a licença a partir de um objeto de stream

O exemplo a seguir mostra como carregar uma licença a partir de um stream.

```java
// Inicializar Instância de Licença
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Definir licença a partir do Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Definindo uma Licença Adquirida Antes de 22/01/2005**Aspose.PDF** para Java não suporta mais licenças antigas, então, por favor, entre em contato com nosso [time de vendas](https://company.aspose.com/contact) para obter um novo arquivo de licença.

### Validar a Licença

É possível validar se a licença foi configurada corretamente ou não. A classe Document possui o método isLicensed que retornará true se a licença foi configurada corretamente.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Verifique se a licença foi validada
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Licença Medida

Aspose.PDF permite que os desenvolvedores apliquem uma chave medida. É um novo mecanismo de licenciamento. O novo mecanismo de licenciamento será usado junto com o método de licenciamento existente. Aqueles clientes que desejam ser cobrados com base no uso dos recursos da API podem usar o licenciamento medido. Para mais detalhes, por favor, consulte a seção [FAQ de Licenciamento Medido](https://purchase.aspose.com/faqs/licensing/metered).

Uma nova classe [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) foi introduzida para aplicar a chave medida.
 A seguir está o código de exemplo que demonstra como definir a chave pública e privada medida.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Opcionalmente, as duas linhas a seguir retornam verdadeiro se uma licença válida foi aplicada;
// falso se o componente estiver em modo de avaliação.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Usando Múltiplos Produtos da Aspose

Se você usar vários produtos Aspose em sua aplicação, por exemplo, Aspose.PDF e Aspose.Words, aqui estão algumas dicas úteis.

- **Defina a Licença para cada Produto Aspose Separadamente.** Mesmo que você tenha um único arquivo de licença para todos os componentes, por exemplo 'Aspose.Total.lic', você ainda precisará chamar **License.SetLicense** separadamente para cada produto Aspose que você está usando em sua aplicação.
- **Use o Nome da Classe de Licença Totalmente Qualificado.** Cada produto Aspose tem uma classe **License** em seu namespace. Por exemplo, Aspose.PDF tem a classe **com.aspose.pdf.License** e Aspose.Words tem a classe **com.aspose.words.License**. Usar o nome de classe totalmente qualificado permite que você evite qualquer confusão sobre qual licença é aplicada a qual produto.

```java
// Instanciar a classe License do Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Definir a licença
license.setLicense("Aspose.Total.Java.lic");

// Configurando a licença para Aspose.Words para Java

// Instanciar a classe License do Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Definir a licença
licenseaw.setLicense("Aspose.Total.Java.lic");
```