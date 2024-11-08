---
title: Aspose.PDF para .NET via COM Interop
type: docs
weight: 20
url: /pt/net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

As informações neste tópico aplicam-se a cenários nos quais você deseja usar [Aspose.PDF para .NET](/pdf/pt/net/) via COM Interop em qualquer uma das seguintes linguagens de programação:

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

Aspose.PDF para .NET é executado sob o controle do .NET Framework e isso é chamado de código gerenciado. O código escrito em todas as linguagens acima é executado fora do .NET Framework e é chamado de código não gerenciado. A interação entre o código não gerenciado e o Aspose.PDF ocorre através de uma funcionalidade do .NET chamada COM Interop.

Os objetos Aspose.PDF são objetos .NET, mas, quando usados via COM Interop, aparecem como objetos COM na sua linguagem de programação.
Os objetos Aspose.PDF são objetos .NET, mas quando usados via COM Interop, eles aparecem como objetos COM no seu idioma de programação.

{{% alert color="primary" %}}

- No mundo COM distinguimos servidor COM e cliente COM. O servidor COM armazena classes COM enquanto o cliente COM solicita instâncias de classes, ou seja, objetos COM.
- O cliente COM ou simplesmente aplicação cliente pode saber algo sobre o conteúdo da classe COM ou ser totalmente ignorante sobre seus métodos e propriedades. Portanto, a aplicação cliente pode descobrir a estrutura da classe COM ao compilar/construir ou somente durante a execução. O processo de "descoberta" é conhecido como vinculação e, assim, temos **vinculação precoce** e **vinculação tardia**.
- Em resumo, a classe COM é como uma caixa preta e para trabalhar com ela é necessário uma biblioteca de tipos, este arquivo binário tem descrição dos métodos, propriedades da classe COM e qualquer linguagem de alto nível que suporte trabalhar com objetos COM frequentemente tem expressão sintática para adicionar biblioteca de tipos, por exemplo, isto é [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) em C++.
- Em resumo, a classe COM é como uma caixa preta e, para trabalhar com ela, é necessária uma biblioteca de tipos. Esse arquivo binário possui descrição dos métodos e propriedades da classe COM, e qualquer linguagem de alto nível que suporte a trabalhar com objetos COM geralmente tem uma expressão sintática para adicionar a biblioteca de tipos, por exemplo, isto é [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) em C++.
- A biblioteca de tipos é usada para vinculação antecipada.
- Um objeto COM pode expor seus métodos e propriedades de duas maneiras: por meio de uma **interface de despacho** (dispinterface) e em sua **tabela de funções virtuais** (vtable).
- Dentro da **dispinterface**, cada método e propriedade é identificado por um membro único; esse membro é o identificador de despacho da função (ou **DispID**).
- **vtable** é apenas um conjunto de ponteiros para funções que a interface da classe COM suporta.
- Um objeto que expõe seus métodos por meio de ambas as interfaces suporta uma **interface dupla**.
- Existem vantagens em ambos os tipos de vinculação.
- existem vantagens em ambos os tipos de vinculação.
- o mecanismo de vinculação tardia tem uma grande vantagem: se o criador da DLL COM decidir lançar uma nova versão, com um layout de interface de função diferente, qualquer código que chame esses métodos não vai falhar, a menos que os métodos não estejam mais disponíveis; mesmo que a **vtable** seja diferente, a vinculação tardia consegue descobrir os novos DISPIDs e chamar os métodos apropriados.
{{% /alert %}}

Aqui estão os tópicos que você eventualmente precisará dominar:
{{% alert color="primary" %}}

- Usando objetos COM na sua linguagem de programação. Consulte a documentação da sua linguagem de programação e os tópicos específicos da linguagem mais adiante nesta documentação.

- Trabalhando com objetos COM expostos pelo .NET COM Interop. Veja [Interoperando com Código Não Gerenciado](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) e [Expondo Componentes do .NET Framework para COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) no MSDN.

- Modelo de objeto de documento Aspose.PDF.
- Modelo de objetos de documento Aspose.PDF.

{{% /alert %}}

## Registrar o Aspose.PDF para .NET com COM Interop

Você precisa instalar o Aspose.PDF para .NET e garantir que ele está registrado com COM Interop (garantindo que ele possa ser chamado a partir de código não gerenciado).

{{% alert color="primary" %}}

Para registrar manualmente o Aspose.PDF para .NET para COM Interop:

1. No menu **Iniciar**, selecione **Todos os Programas**, depois **Microsoft Visual Studio**, **Ferramentas do Visual Studio** e, finalmente, **Prompt de Comando do Visual Studio**.
1. Digite o comando para registrar o assembly:
   1. .NET Framework 2.0
      regasm "C:\Arquivos de Programas\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Arquivos de Programas\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Arquivos de Programas\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Preste atenção que a opção /codebase é necessária apenas se o Aspose.PDF.dll não estiver no GAC, usando essa opção faz com que o regasm coloque o caminho para o assembly no registro.
{{% alert color="primary" %}}

regasm.exe é uma ferramenta incluída no SDK do .NET Framework. Todas as ferramentas do SDK do .NET Framework estão localizadas no diretório *\Microsoft .NET\Framework\<VersãoDoFramework>*, por exemplo *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Se você usa o Visual Studio .NET:
No menu **Iniciar**, selecione **Programas**, seguido por **Microsoft Visual Studio .NET**, depois **Ferramentas do Visual Studio .NET** e, finalmente, **Prompt de Comando do Visual Studio .NET 2003**.
Ele executa um prompt de comando com todas as variáveis de ambiente necessárias configuradas.

{{% /alert %}}

### ProgIDs

ProgID significa "identificador programático". É o nome de uma classe COM que é usada para criar um objeto. Os ProgIDs consistem no nome da biblioteca "Aspose.PDF" e no nome da classe.

### Biblioteca de Tipos

{{% alert color="primary" %}}

Se a sua linguagem de programação (por exemplo, Visual Basic ou Delphi) permite que você faça referência a uma biblioteca de tipos COM, então adicione uma referência ao Aspose.PDF.tlb e para ver todas as classes, métodos, propriedades e enumerações do Aspose.PDF para .NET no seu Navegador de Objetos.
Se a sua linguagem de programação (por exemplo, Visual Basic ou Delphi) permitir que você referencie uma biblioteca de tipos COM, então adicione uma referência ao Aspose.PDF.tlb e para ver todas as classes, métodos, propriedades e enumerações do Aspose.PDF para .NET no seu Navegador de Objetos.

Para gerar um arquivo TLB:

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Criando Objetos COM

A criação de um objeto COM é semelhante à criação de um objeto .NET normal:

```vb

'Instancie a instância Pdf chamando seu construtor vazio

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
Uma vez criado, você poderá acessar os métodos e propriedades do objeto, como se fosse um objeto COM:

```vb
'Adicionar seção ao objeto Pdf
pdf.Sections.Add(pdfsection)
```

Alguns métodos têm sobrecargas e serão expostos pelo COM Interop com um sufixo numérico adicionado a eles, exceto pelo primeiro método que permanece inalterado. Por exemplo, as sobrecargas do método Pdf.Save tornam-se Pdf.Save, Pdf.Save_2 e assim por diante.

Para mais informações, consulte os artigos específicos do idioma mais adiante nesta documentação.

## Criando um Assembly de Invólucro

Se você precisa usar muitas classes, métodos e propriedades do Aspose.PDF para .NET, considere criar um assembly de invólucro (usando C# ou qualquer outra linguagem de programação .NET). Assemblies de invólucro ajudam a evitar o uso direto do Aspose.PDF para .NET a partir de código não gerenciado.

Uma boa abordagem é desenvolver um assembly .NET que referencia o Aspose.PDF para .NET e faz todo o trabalho com ele, e expõe apenas um conjunto mínimo de classes e métodos para o código não gerenciado.
Uma boa abordagem é desenvolver uma assembly .NET que referencia o Aspose.PDF para .NET e faz todo o trabalho com ele, expondo apenas um conjunto mínimo de classes e métodos para o código não gerenciado.

Reduzir o número de classes e métodos que você precisa invocar via COM Interop simplifica o projeto. Usar classes .NET via COM Interop frequentemente requer habilidades avançadas.
