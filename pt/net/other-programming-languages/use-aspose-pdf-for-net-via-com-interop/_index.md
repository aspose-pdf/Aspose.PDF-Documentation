---
title: Aspose.PDF para .NET via COM Interop
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /pt/net/use-aspose-pdf-for-net-via-com-interop/
description: Descubra como usar Aspose.PDF for .NET via COM Interop para integração perfeita com aplicativos que não são .NET.
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF for .NET via COM Interop",
    "alternativeHeadline": "Aspose.PDF for .NET Enables COM Interop Usage",
    "abstract": "Aspose.PDF for .NET agora suporta integração perfeita com várias linguagens de programação através do COM Interop, permitindo que os desenvolvedores utilizem suas poderosas capacidades de manipulação de PDF fora do framework .NET. Este recurso aumenta a flexibilidade ao transformar objetos Aspose.PDF em objetos COM, simplificando interações com código não gerenciado enquanto mantém alto desempenho através de técnicas de vinculação antecipada e tardia.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1338",
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
    "url": "/net/use-aspose-pdf-for-net-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/use-aspose-pdf-for-net-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

As informações neste tópico se aplicam a cenários onde você deseja usar [Aspose.PDF for .NET](/pdf/pt/net/) via COM Interop em qualquer uma das seguintes linguagens de programação:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Trabalhando com COM Interop

Aspose.PDF for .NET é executado sob o controle do .NET Framework e isso é chamado de código gerenciado. O código escrito em todas as linguagens acima é executado fora do .NET Framework e é chamado de código não gerenciado. A interação entre código não gerenciado e Aspose.PDF ocorre através do recurso .NET chamado COM Interop.

Os objetos Aspose.PDF são objetos .NET, mas quando usados via COM Interop, eles aparecem como objetos COM em sua linguagem de programação. Portanto, é melhor garantir que você saiba como criar e usar objetos COM em sua linguagem de programação, antes de começar a usar [Aspose.PDF for .NET](/pdf/pt/net/).

{{% alert color="primary" %}}

- No mundo COM, distinguimos entre servidor COM e cliente COM. O servidor COM armazena classes COM enquanto o cliente COM solicita instâncias de classes ao servidor COM, ou seja, objetos COM.
- O cliente COM ou simplesmente aplicativo cliente pode saber algo sobre o conteúdo da classe COM ou estar totalmente alheio aos seus métodos e propriedades. Portanto, o aplicativo cliente pode descobrir a estrutura da classe COM durante a compilação/construção ou apenas durante a execução. O processo de "descoberta" é conhecido como vinculação e assim temos **vinculação antecipada** e **vinculação tardia**.
- em resumo, a classe COM é como uma caixa preta e para trabalhar com ela, uma biblioteca de tipos é necessária; este arquivo binário tem a descrição dos métodos, propriedades da classe COM e qualquer linguagem de alto nível que suporte trabalhar com objetos COM frequentemente tem uma expressão de sintaxe para adicionar a biblioteca de tipos, por exemplo, isso é [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) em C++.
- a biblioteca de tipos é usada para vinculação antecipada.
- um objeto COM pode expor seus métodos e propriedades de duas maneiras: por meio de uma **interface de despacho** (dispinterface) e em sua **vtable** (tabela de funções virtuais).
- dentro da **dispinterface**, cada método e propriedade é identificado por um membro único; esse membro é o identificador de despacho da função (ou **DispID**).
- **vtable** é apenas um conjunto de ponteiros para funções que a interface da classe COM suporta.
- um objeto que expõe seus métodos através de ambas as interfaces suporta uma **interface dupla**.
- existem vantagens em ambos os tipos de vinculação. A vinculação antecipada fornece a você um desempenho aumentado e verificação de sintaxe em tempo de compilação. A vinculação tardia é mais vantajosa quando você está escrevendo clientes que pretende que sejam ***compatíveis com versões futuras*** de sua classe COM. Com a vinculação tardia, as informações da biblioteca de tipos não estão "hard-wired" em seu cliente, então você pode ter maior confiança de que seu cliente pode trabalhar com versões futuras da classe COM sem alterações no código.
- o mecanismo de vinculação tardia tem uma grande vantagem: se o criador do DLL COM decidir lançar uma nova versão, com um layout de interface de função diferente, qualquer código que chame esses métodos não irá falhar, a menos que os métodos não estejam mais disponíveis; mesmo que a **vtable** seja diferente, a vinculação tardia consegue descobrir os novos DISPIDs e chamar os métodos apropriados.
{{% /alert %}}

Aqui estão os tópicos que você eventualmente precisará dominar:
{{% alert color="primary" %}}

- Usando objetos COM em sua linguagem de programação. Consulte a documentação da sua linguagem de programação e os tópicos específicos da linguagem mais adiante nesta documentação.

- Trabalhando com objetos COM expostos pelo .NET COM Interop. Veja [Interoperando com Código Não Gerenciado](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) e [Expondo Componentes do .NET Framework para COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) no MSDN.

- Modelo de objeto de documento Aspose.PDF. Veja [Guia do Programador Aspose.PDF](http://www.aspose.com/docs/display/pdfnet/Programmers+Guide) e [Referência da API](http://www.aspose.com/docs/display/pdfnet/Aspose.PDF+for+.NET+API+Reference).

{{% /alert %}}

## Registrar Aspose.PDF for .NET com COM Interop

Você precisa instalar Aspose.PDF for .NET e garantir que ele esteja registrado com COM Interop (assegurando que pode ser chamado a partir de código não gerenciado).

{{% alert color="primary" %}}

Para registrar Aspose.PDF for .NET para COM Interop manualmente:

1. No menu **Iniciar**, selecione **Todos os Programas**, depois **Microsoft Visual Studio**, **Ferramentas do Visual Studio** e, finalmente, **Prompt de Comando do Visual Studio**.
1. Digite o comando para registrar a assembly:
   1. .NET Framework 4.8.1
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /codebase
   1. .NET 6.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /codebase
   1. .NET 7.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /codebase
   1. .NET 8.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /codebase
   1. .NET Standard 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Preste atenção que /codebase é necessário apenas se Aspose.PDF.dll não estiver no GAC, usar esta opção faz com que regasm coloque o caminho da assembly no registro.

{{% alert color="primary" %}}

regasm.exe é uma ferramenta incluída no SDK do .NET Framework. Todas as ferramentas do SDK do .NET Framework estão localizadas no diretório *\Microsoft .NET\Framevork\<FrameworkVersion>*, por exemplo *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Se você usar o Visual Studio .NET:
No menu **Iniciar**, selecione **Programas**, seguido por **Visual Studio 2022**, finalmente, **Prompt de Comando do Desenvolvedor para VS 2022**.
Isso executa um prompt de comando com todas as variáveis de ambiente necessárias configuradas.

{{% /alert %}}

### ProgIDs

ProgID significa “identificador programático”. É o nome de uma classe COM que é usada para criar um objeto. ProgIDs consistem no nome da biblioteca "Aspose.PDF" e no nome da classe.

### Biblioteca de Tipos

{{% alert color="primary" %}}

Se sua linguagem de programação (por exemplo, Visual Basic ou Delphi) permitir que você faça referência a uma biblioteca de tipos COM, então adicione uma referência a Aspose.PDF.tlb e veja todas as classes, métodos, propriedades e enumerações de Aspose.PDF for .NET em seu Navegador de Objetos.

Para gerar um arquivo TLB:

- .NET Framework 4.8.1
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.8.1\Aspose.PDF.tlb" /codebase
- .NET 6.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net6.0\Aspose.PDF.tlb" /codebase
- .NET 7.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net7.0\Aspose.PDF.tlb" /codebase
- .NET 8.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net8.0\Aspose.PDF.tlb" /codebase
- .NET Standard 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\netstandard2.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Criando Objetos COM

A criação de um objeto COM é semelhante à criação de um objeto .NET normal:

```vb
'Instantiate Pdf instance by calling its empty constructor
Dim document
Set document = CreateObject("Aspose.Pdf.Document")

```

Uma vez criado, você pode acessar os métodos e propriedades do objeto, como se fosse um objeto COM:

```vb
'Add page to the document
document.Pages.Add()
```

Alguns métodos têm sobrecargas e elas serão expostas pelo COM Interop com um sufixo numérico adicionado a elas, exceto pelo primeiro método que permanece inalterado. Por exemplo, as sobrecargas do método Document.Save tornam-se Document.Save, Document.Save_2, e assim por diante.

Para mais informações, consulte os artigos específicos da linguagem mais adiante nesta documentação.

## Criando uma Assembly Wrapper

Se você precisar usar muitas classes, métodos e propriedades de Aspose.PDF for .NET, considere criar uma assembly wrapper (usando C# ou qualquer outra linguagem de programação .NET). Assemblies wrapper ajudam a evitar o uso de Aspose.PDF for .NET diretamente a partir de código não gerenciado.

Uma boa abordagem é desenvolver uma assembly .NET que faça referência a Aspose.PDF for .NET e faça todo o trabalho com ela, e apenas exponha um conjunto mínimo de classes e métodos para código não gerenciado. Seu aplicativo deve então funcionar apenas com sua biblioteca wrapper.

Reduzir o número de classes e métodos que você precisa invocar via COM Interop simplifica o projeto. Usar classes .NET via COM Interop frequentemente requer habilidades avançadas.