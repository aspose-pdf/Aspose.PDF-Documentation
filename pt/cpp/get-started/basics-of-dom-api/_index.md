---
title: Noções básicas da API DOM do Aspose.PDF
linktitle: Noções básicas da API DOM
type: docs
weight: 120
url: /pt/cpp/basics-of-dom-api/
description: O Aspose.PDF para C++ também usa a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos. Aqui você pode ler a descrição dessa estrutura.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introdução à API DOM

O Modelo de Objeto de Documento (DOM) é uma forma de representação de documentos estruturados como um modelo orientado a objetos. O DOM é o padrão oficial do World Wide Web Consortium (W3C) para representar documentos estruturados de maneira neutra em termos de plataforma e linguagem.

Em palavras simples, o DOM é uma árvore de objetos que representam a estrutura de algum documento. Aspose.PDF for C++ também usa a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos. No entanto, os aspectos do DOM (como seus Elementos) são manipulados dentro da sintaxe da linguagem de programação em uso. A interface pública de um DOM é especificada em sua interface de programação de aplicativos (API).

### Introdução ao Documento PDF

O formato de documento portátil (PDF) é um padrão aberto para troca de documentos. Um documento PDF é uma combinação de dados de texto e binário. Se você abri-lo em um editor de texto, verá os objetos brutos que definem a estrutura e o conteúdo do documento.

A estrutura lógica de um arquivo PDF é hierárquica e determina a sequência pela qual um aplicativo de visualização desenha as páginas do documento e seu conteúdo. Um PDF é composto por quatro componentes: objetos, estrutura de arquivo, estrutura de documento e fluxos de conteúdo.

### Estrutura do Documento PDF

Como a estrutura de um arquivo PDF é hierárquica, o Aspose.PDF para C++ também acessa os elementos da mesma forma. A hierarquia a seguir mostra como o documento PDF é estruturado logicamente e como o Aspose.PDF para C++ DOM API o constrói.

![Estrutura do Documento PDF](../images/structure.png)

### Acessando Elementos do Documento PDF

O objeto Documento está no nível raiz do modelo de objeto. O Aspose.PDF para C++ DOM API permite que você crie um objeto Documento e, em seguida, acesse todos os outros objetos na hierarquia. Você pode acessar qualquer uma das coleções como Páginas ou um elemento individual como Página, etc. A API DOM fornece pontos únicos de entrada e saída para manipular o documento PDF, conforme mostrado abaixo:

- Abrir documento PDF
- Acessar a estrutura do documento PDF no estilo DOM
- Atualizar dados no documento PDF
- Validar documento PDF
- Exportar documento PDF em diferentes formatos
- Finalmente, salvar o documento PDF atualizado

## Como Usar o Novo Aspose.PDF para C++ API

Este tópico explicará o novo Aspose.PDF para C++ API e irá guiá-lo para começar rapidamente e facilmente. Por favor, note que os detalhes sobre o uso dos recursos particulares não fazem parte deste artigo.

O Aspose.PDF para C++ é composto por duas partes:

- Aspose.PDF para C++ DOM API
- Aspose.PDF.Facades

Você encontrará os detalhes de cada uma dessas áreas abaixo.

### Aspose.PDF para C++ DOM API

O Aspose.PDF para C++ DOM API corresponde à estrutura do documento PDF, o que ajuda você a trabalhar com documentos PDF não apenas no nível de arquivo e documento, mas também no nível de objeto. Nós fornecemos mais flexibilidade aos desenvolvedores para acessar todos os elementos e objetos do documento PDF. Usando as classes da API Aspose.PDF DOM, você pode obter acesso programático aos elementos e formatação do documento. Esta nova API DOM é composta por vários namespaces conforme dado abaixo:

### Aspose::Pdf Namespace Reference

Este namespace fornece a classe Document que permite abrir e salvar um documento PDF.

#### Aspose::Pdf::Text Namespace Reference

Este namespace fornece classes que ajudam você a trabalhar com o texto e seus vários aspectos, por exemplo, Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment e TextSegmentCollection, etc.
#### Aspose::Pdf::Collections Namespace Reference

Este namespace fornece a classe AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

Este namespace fornece as classes: Curve, Circle, Arc, Rectangle, Graph e etc., para adicionar elementos gráficos ao seu arquivo PDF.

#### Aspose::Pdf::Engine Namespace Reference

Este namespace fornece as classes Addressing, Interactive, Security, CommonData, IO, Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

Este namespace fornece as classes: ExtractorFactory - representa uma fábrica para criar objetos IPdfTypeExtractor, IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor classes - representa a interface para interagir com o extrator.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

Este namespace fornece as classes: AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement, e etc.

#### Aspose::Pdf::Operators Namespace Reference

Este namespace fornece classes dos seguintes operadores: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator, etc.

#### Aspose::Pdf::Optimization Namespace Reference

Este namespace fornece duas classes - ImageCompressionOptions e OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

Este namespace fornece duas classes: FontEmbeddingOptions - o padrão PDF/A exige que todas as fontes sejam incorporadas no documento. Esta classe inclui flags para casos em que não é possível incorporar alguma fonte devido a essa fonte estar ausente no PC de destino. ToUnicodeProcessingRules - Esta classe descreve regras que podem ser usadas para resolver o erro do Adobe Preflight "Texto não pode ser mapeado para Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

Este namespace fornece duas classes: Details_SanitizationException e IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

Este namespace fornece classes Details_TaggedException - Representa exceção para o conteúdo TaggedPDF do documento. ITaggedContent - Representa interface para trabalhar com o conteúdo TaggedPdf do documento? e TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

Este namespace fornece a classe XfaParserOptions - classe para lidar com encapsulamento de dados relacionados.

#### Aspose::Pdf::Annotations Namespace Reference

Anotações são uma parte dos recursos interativos de um documento PDF. Dedicamos um namespace para anotações. Este namespace contém classes que ajudam você a trabalhar com as anotações, por exemplo, Annotation, AnnotationCollection, CircleAnnotation e LinkAnnotation, etc.

#### Aspose::Pdf::Forms Namespace Reference

Este namespace contém classes que ajudam você a trabalhar com formulários PDF e campos de formulário, por exemplo Form, Field, TextBoxField e OptionCollection, etc.

#### Aspose::Pdf::Devices Namespace Reference

Podemos realizar várias operações nos documentos PDF, como converter documentos PDF em vários formatos de imagem. No entanto, tais operações não pertencem ao objeto Documento e não podemos estender a classe Documento para essas operações. É por isso que introduzimos o conceito de Dispositivo na nova API DOM.

##### Referência do Namespace Aspose::Pdf::Facades

Você pode usar o namespace Aspose.PDF.Facades. Este Namespace fornece classes como AutoFiller - representa uma classe para receber dados de um banco de dados ou outra fonte de dados. Bookmark, Form, Stamp, PdfConverter e mais classes.