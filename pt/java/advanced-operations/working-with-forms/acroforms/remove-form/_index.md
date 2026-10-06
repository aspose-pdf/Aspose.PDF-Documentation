---
title: Excluir formulários de PDF em Java
linktitle: Excluir formulários
type: docs
weight: 70
url: /pt/java/remove-form/
description: Remover objetos de formulário de páginas PDF usando Aspose.PDF for Java, incluindo limpeza completa e exclusão direcionada.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover recursos de formulário de páginas PDF com Java
Abstract: Este artigo explica como remover recursos de formulário de documentos PDF usando Aspose.PDF for Java. Ele aborda a limpeza de todos os formulários de uma página e a exclusão apenas dos recursos de formulário Typewriter selecionados após filtrar a coleção de formulários da página.
---
Esses exemplos removem recursos de formulário de uma página, em vez de apenas alterar valores de campo.

## Remover todos os recursos de formulário de uma página

Use este exemplo quando todos os recursos de formulário em uma página selecionada devem ser removidos em uma única operação.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar o [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para a página de destino.
1. Limpe a coleção e salve o documento atualizado.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## Remover recursos de Form específicos

Use este exemplo quando apenas recursos de Form selecionados, como Typewriter forms, devem ser excluídos.

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar o [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) para a página de destino.
1. Filtrar o [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) recursos que você deseja remover e excluí-los da coleção.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
