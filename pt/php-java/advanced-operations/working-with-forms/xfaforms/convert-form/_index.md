---
title: Converter Formulário XFA para AcroForm
linktitle: Converter Formulário XFA
type: docs
weight: 10
url: pt/php-java/convert-form/
description: Esta seção explica como converter Formulário XFA para AcroForm com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Converter Formulário XFA Dinâmico para AcroForm Padrão

Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a “Arquitetura de Formulários XML”. Também pode converter formulário XFA dinâmico para Acroform padrão. A informação sobre o formulário (no que diz respeito ao PDF) é muito vaga – especifica que campos existem, com propriedades e eventos JavaScript, mas não especifica nenhuma renderização. Os objetos do formulário XFA são desenhados no momento em que o documento é carregado.

Atualmente, o PDF suporta dois métodos diferentes para integrar dados e formulários PDF:

- AcroForms (também conhecidos como formulários Acrobat), introduzidos e incluídos na especificação do formato PDF 1.2.

- Formulários Adobe XML Forms Architecture (XFA), introduzidos na especificação de formato PDF 1.5 como um recurso opcional. (A especificação XFA não está incluída na especificação PDF, ela é apenas referenciada.)

Não é possível extrair ou manipular páginas de Formulários XFA, porque o conteúdo do formulário é gerado em tempo de execução (durante a visualização do formulário XFA) dentro do aplicativo que tenta exibir ou renderizar o formulário XFA. Aspose.PDF tem um recurso que permite aos desenvolvedores converter formulários XFA em AcroForms padrão.

```php

        // Carregar formulário XFA
        $document = new Document($inputFile);
        
        // Definir o tipo de campos do formulário como AcroForm padrão
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // Salvar o documento atualizado
        $document->save($outputFile);
        
        // Salvar PDF modificado    
        $document->close();
```