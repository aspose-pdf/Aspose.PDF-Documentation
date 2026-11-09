---
title: Adicionar cabeçalhos e rodapés de PDF em Java
linktitle: Adicionar cabeçalhos e rodapés
type: docs
weight: 70
url: /pt/java/artifacts-header-footer/
description: Criar artefatos de cabeçalho e rodapé estilizados e adicioná-los às páginas de PDF em Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar cabeçalhos e rodapés em Java
Abstract: Criar artefatos de cabeçalho e rodapé estilizados e adicioná-los às páginas de PDF em Java.
---
Os artefatos de cabeçalho e rodapé são elementos de paginação não relacionados ao conteúdo, comumente usados para rótulos repetidos, identificadores de página e enquadramento de layout.

## Criar um artefato de cabeçalho

Use este auxiliar quando precisar de um artefato de cabeçalho reutilizável com estilo de texto consistente e alinhamento.

1. Crie um [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Defina seu texto, configurações de fonte e cor de primeiro plano.
1. Configure o alinhamento horizontal e retorne o artefato.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Criar um artefato de rodapé

Este auxiliar cria um artefato de rodapé reutilizável com o mesmo padrão de estilo do artefato de cabeçalho.

1. Crie um [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Defina seu texto, estado do texto e cor de primeiro plano.
1. Configure o alinhamento e retorne o artefato.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Adicione um artefato de cabeçalho

Use este exemplo quando uma página deve exibir um artefato de cabeçalho reutilizável.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o artefato de cabeçalho usando o método auxiliar.
1. Adicione o artefato à página e salve o arquivo de saída.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Adicionar um artefato de rodapé

Use este exemplo quando a página deve exibir um artefato de rodapé com formatação reutilizável.

1. Abra o PDF de origem com [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o artefato de rodapé usando o método auxiliar.
1. Adicione o artefato à página e salve o arquivo de saída.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Tópicos relacionados

- [Remover cabeçalhos e rodapés](/pdf/pt/java/remove-headers-footers/)
- [Trabalhar com artefatos PDF em Java](/pdf/pt/java/artifacts/)
