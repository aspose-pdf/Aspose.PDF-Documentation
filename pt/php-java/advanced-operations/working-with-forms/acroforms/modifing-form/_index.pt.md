---
title: Modificando AcroForms
linktitle: Modificando AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: Esta seção explica como modificar formulários no seu documento PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Definir Fonte Personalizada para Campo de Formulário

Os campos de formulário em arquivos PDF do Adobe podem ser configurados para usar fontes padrão específicas. O Aspose.PDF permite que os desenvolvedores apliquem qualquer fonte como fonte padrão de campo, seja uma das 14 fontes principais ou uma fonte personalizada.
Para definir e atualizar a fonte padrão usada para campos de formulário, o Aspose.PDF possui a classe DefaultAppearance (Font font, double size, Color color). Esta classe pode ser acessada usando com.aspose.pdf.DefaultAppearance. Para usar este objeto, utilize o método setDefaultAppearance(..) da classe Field.

O trecho de código a seguir mostra como definir a fonte padrão para o campo de formulário PDF.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Criar objeto de fonte
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Definir as informações de fonte para o campo de formulário
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Salvar documento atualizado
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Get/Set FieldLimit

Este código demonstra o uso da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para abrir um documento, recuperar um campo de formulário, definir seu comprimento máximo, recuperar o comprimento máximo com os métodos 'setMaxLen' e 'getMaxLen'.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter um campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Obtendo o limite máximo do campo usando DOM
    $responseData = "Limite: " . $field->getMaxLen();          

    $document->close();
```

Você também pode obter o mesmo valor usando o namespace Aspose.PDF.Facades usando o seguinte trecho de código.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter um campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Obtendo o limite máximo do campo usando DOM
    $responseData = "Limite: " . $field->getMaxLen();          

    $document->close();
```


Similarmente, o Aspose.PDF tem um método que obtém o limite do campo usando a abordagem DOM. O seguinte trecho de código mostra os passos.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Excluir campo
    $field->delete();
    
    $document->close();
```
## Excluir um Campo de Formulário Específico de um Documento PDF

Todos os campos do formulário estão contidos na coleção Form do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Esta coleção fornece diferentes métodos que gerenciam campos de formulário, incluindo o método de exclusão. Se você quiser excluir um campo específico, passe o nome do campo como parâmetro para o método de exclusão e, em seguida, salve o documento PDF atualizado.

O seguinte trecho de código mostra como excluir um campo nomeado de um documento PDF.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Excluir campo
    $field->delete();
    
    $document->close();
```


## Modificar Campo de Formulário em um Documento PDF

A coleção Formulário do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) permite gerenciar campos de formulário em um documento PDF.

Para modificar um campo de formulário, obtenha o campo da coleção Formulário e defina suas propriedades. Em seguida, salve o documento PDF atualizado.

O trecho de código a seguir mostra como modificar um campo de formulário existente em um documento PDF.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter um campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Modificar o valor do campo
    $field->setValue("Valor Atualizado");

    // Definir o campo como somente leitura
    $field->setReadOnly(true);

    // Salvar o documento atualizado
    $document->save($outputFile);        
    $document->close();
```

### Mover Campo de Formulário para uma Nova Localização em um Arquivo PDF

Se você deseja mover um campo de formulário para uma nova localização em uma página PDF, primeiro obtenha o objeto do campo e, em seguida, especifique um novo valor para seu método setRect.
 Um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) com novas coordenadas é atribuído ao método setRect(..). Em seguida, salve o PDF atualizado usando o método save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra como mover um campo de formulário para uma nova localização.

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter campo de formulário específico do documento
    $field = $document->getForm()->get("textbox1");

    // Modificar a localização do campo
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Salvar o documento atualizado
    $document->save($outputFile);        
    $document->close();
```