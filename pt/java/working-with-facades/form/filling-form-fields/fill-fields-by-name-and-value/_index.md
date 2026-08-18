---
title: Preencha os campos por nome e valor
linktitle: Preencha os campos por nome e valor
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: Aprenda como adaptar a API de preenchimento de campo de fachada de formulário em Java para atualizações dinâmicas de formulário de nome-valor.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Preencha vários campos de formulário PDF a partir de pares nome-valor em Java
Abstract: O conjunto de amostra Java atual preenche os campos individualmente com chamadas `fillField(...)` repetidas. Este artigo mostra como aplicar o mesmo padrão de API à sua própria coleção nome-valor sem inventar um recurso de fachada separado que não está presente nos exemplos do repositório.
---
A classe Java `FormExamples` preenche campos individuais diretamente:

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

Se seu aplicativo já possui um conjunto dinâmico de nomes e valores de campos, aplique a mesma chamada `fillField(...)` dentro de seu próprio loop:

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

Este é um padrão de nível de aplicativo derivado da mesma API Java usada em `FormExamples.fillTextFields(...)`; o repositório atual não inclui um método auxiliar dedicado separado para preenchimento baseado em mapa.
