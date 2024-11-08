---
title: Trabalhando com AcroForms em PDF
linktitle: AcroForms
type: docs
weight: 10
url: /pt/php-java/acroforms/
description: Com o Aspose.PDF para PHP via Java, você pode criar um formulário do zero, preencher o campo do formulário em um documento PDF, extrair dados do formulário, adicionar ou remover campos no formulário existente.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fundamentos dos AcroForms

**AcroForms** são a tecnologia original de formulários PDF. AcroForms é um formulário orientado por página. Eles foram introduzidos pela primeira vez em 1998. Eles aceitam entrada no Formato de Dados de Formulários ou FDF e no Formato de Dados de Formulários XML ou xFDF. Fornecedores de terceiros dão suporte aos AcroForms. Quando a Adobe introduziu os AcroForms, eles os chamaram de “formulário PDF que é criado com o Adobe Acrobat Pro/Standard e que não é um tipo especial de formulário XFA estático ou dinâmico. Acroforms são portáteis e funcionam em todas as plataformas.

Você pode usar AcroForms para adicionar páginas adicionais ao documento de formulário PDF.
 Graças ao conceito de Modelos, você pode usar AcroForms para apoiar o preenchimento do formulário com múltiplos registros de banco de dados.

O PDF 1.7 suporta dois métodos diferentes para integrar dados e formulários PDF.

*AcroForms (também conhecidos como formulários Acrobat)*, introduzidos e incluídos na especificação do formato PDF 1.2.

*Formulários Adobe XML Forms Architecture (XFA)*, introduzidos na especificação do formato PDF 1.5 como um recurso opcional. A especificação XFA não está incluída na especificação do PDF, apenas é referenciada.

Para entender **Acroforms** vs formulários **XFA**, precisamos entender o básico primeiro. Para começar, ambos são formulários PDF que você pode usar. Acroforms é o mais antigo, criado em 1998, e ainda é referido como o formulário PDF clássico. Os formulários XFA são páginas da web que você pode salvar como PDF, e apareceram em 2003. Levou algum tempo antes que o PDF começasse a aceitar formulários XFA.

AcroForms têm capacidades que não são encontradas em XFA e, inversamente, XFA tem algumas capacidades que não são encontradas em AcroForms. Por exemplo:

- AcroForms suportam o conceito de “Modelos”, permitindo que páginas adicionais sejam adicionadas ao documento de formulário PDF para apoiar o preenchimento do formulário com múltiplos registros de banco de dados.- XFA suporta o conceito de reflow de documento, permitindo que um campo seja redimensionado, se necessário, para acomodar dados.

Portanto, PDFs são o melhor formato de arquivo para formulários, pois podem ser distribuídos eletronicamente e ter informações preenchidas dentro do documento e enviadas de volta ao remetente sem a necessidade de imprimir ou enviar pelo correio tradicional.

Para um estudo mais detalhado das possibilidades de trabalhar com formulários, estude os seguintes artigos na seção:

-[Criar AcroForm](/pdf/pt/php-java/create-form/) - criar formulário do zero, adicionando RadioButtonField, TextBoxField, Caption Field usando PHP.

-[Preencher AcroForm](/pdf/pt/php-java/fill-form/) - para preencher um campo de formulário, obtenha o campo da coleção de Formulários do objeto Document.

-[Extrair Dados AcroForm](/pdf/pt/php-java/extract-form/) - obter valores de todos e dos campos individuais, etc.

-[Modificar AcroForm](/pdf/pt/php-java/modifing-form/) - obter/definir FieldLimit, remover campos em formulários existentes, definir a fonte do campo de formulário diferente das 14 Fontes Core PDF com PHP.