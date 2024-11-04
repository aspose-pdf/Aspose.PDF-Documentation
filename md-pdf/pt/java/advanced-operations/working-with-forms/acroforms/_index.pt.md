---
title: Trabalhando com AcroForms em PDF 
linktitle: AcroForms
type: docs
weight: 10
url: /java/acroforms/
description: Com o Aspose.PDF para Java, você pode criar um formulário do zero, preencher o campo do formulário em um documento PDF, extrair dados do formulário, adicionar ou remover campos no formulário existente.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fundamentos dos AcroForms

**AcroForms** são a tecnologia original de formulários PDF. AcroForms é um formulário orientado por página. Eles foram introduzidos pela primeira vez em 1998. Eles aceitam entrada em Formato de Dados de Formulários ou FDF e Formato de Dados de Formulários XML ou xFDF. Fornecedores terceiros suportam AcroForms. Quando a Adobe introduziu os AcroForms, eles se referiram a eles como “formulário PDF que é criado com Adobe Acrobat Pro/Standard e que não é um tipo especial de formulário XFA estático ou dinâmico. Acroforms são portáteis e funcionam em todas as plataformas.

Você pode usar AcroForms para adicionar páginas adicionais ao documento do formulário PDF.
 Graças ao conceito de Modelos, você pode usar AcroForms para suportar o preenchimento do formulário com vários registros de banco de dados.

O PDF 1.7 suporta dois métodos diferentes para integrar dados e formulários PDF.

*AcroForms (também conhecidos como formulários Acrobat)*, introduzidos e incluídos na especificação do formato PDF 1.2.

*Formulários da Adobe XML Forms Architecture (XFA)*, introduzidos na especificação do formato PDF 1.5 como um recurso opcional (a especificação XFA não está incluída na especificação PDF, ela é apenas referenciada).

Para entender **Acroforms** vs formulários **XFA**, precisamos entender o básico primeiro. Para começar, ambos são formulários PDF que você pode usar. Acroforms é o mais antigo, criado em 1998, e ainda é referido como o formulário PDF clássico. Os formulários XFA são páginas da web que você pode salvar como PDF, e apareceram em 2003. Levou algum tempo até que o PDF começasse a aceitar formulários XFA.

AcroForms têm capacidades que não são encontradas em XFA e, inversamente, XFA tem algumas capacidades que não são encontradas em AcroForms. Por exemplo:

- AcroForms suportam o conceito de "Modelos", permitindo que páginas adicionais sejam adicionadas ao documento de formulário PDF para suportar o preenchimento do formulário com vários registros de banco de dados.- O XFA suporta o conceito de reflow de documentos, permitindo que um campo redimensione, se necessário, para acomodar os dados.

Portanto, PDFs são o melhor formato de arquivo para formulários, pois podem ser distribuídos eletronicamente e ter informações preenchidas dentro do documento e enviadas de volta ao remetente sem necessidade de impressão ou envio por correio tradicional.

Para um estudo mais detalhado das possibilidades de trabalho com formulários, estude os seguintes artigos na seção:

-[Criar AcroForm](/pdf/java/create-form/) - criar formulário do zero, adicionando RadioButtonField, TextBoxField, Campo de Legenda usando Java.

-[Preencher AcroForm](/pdf/java/fill-form/) - para preencher um campo de formulário, obtenha o campo da coleção de Formulários do objeto Document.

-[Extrair Dados AcroForm](/pdf/java/extract-form/) - obter valores de todos e de campos individuais, etc.

-[Modificar AcroForm](/pdf/java/modifing-form/) - obter/definir FieldLimit, remover campos em formulários existentes, definir fonte de campo de formulário diferente das 14 Fontes PDF Core com Java.