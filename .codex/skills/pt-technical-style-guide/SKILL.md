---
name: pt-br-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Brazilian Portuguese programming documentation. It enforces pt-BR conventions for headings, step-by-step instructions, figure captions, terminology, API identifiers, UI labels, punctuation, and technical formatting.
---

# Brazilian Portuguese Technical Documentation Style

## Goal

Normalize programming documentation written in **Brazilian Portuguese (`pt-BR`)** to a clear, concise, consistent style suitable for developers.

Always use Brazilian Portuguese vocabulary, grammar, spelling, and technical terminology.

Do not mix Brazilian Portuguese with European Portuguese.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved Brazilian Portuguese terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Brazilian Portuguese conventions.

Never change API identifiers, commands, paths, filenames, macros, placeholders, or actual UI labels merely to satisfy a linguistic rule.

---

## 1. Identify the structural role first

Before rewriting text, determine whether it is:

- a task heading;
- a conceptual heading;
- a procedural step;
- a figure caption;
- a note or warning;
- explanatory prose;
- a UI label;
- an API or code identifier.

Do not normalize text mechanically without determining its role.

---

## 2. Use Brazilian Portuguese

Always use Brazilian Portuguese.

Prefer Brazilian forms such as:

| Use in pt-BR | Avoid pt-PT |
|---|---|
| arquivo | ficheiro |
| usuário | utilizador |
| aplicativo | aplicação, when referring specifically to an app |
| salvar | guardar |
| excluir | eliminar/apagar, when the intended action is Delete |
| tela | ecrã |
| mouse | rato |
| baixar / fazer download | descarregar |
| carregar / fazer upload | carregar, according to context |
| gerenciador | gestor, when referring to software management tools |

Do not replace terms mechanically when they have a specific product, API, or UI meaning.

The approved pt-BR glossary always takes precedence.

---

## 3. General writing style

Use concise, direct technical Portuguese.

Prefer active constructions.

Good:

- Este método salva o documento PDF.
- O exemplo a seguir converte um arquivo PDF para DOCX.
- A classe `Document` representa um documento PDF.
- Esta opção controla a qualidade da imagem.

Avoid unnecessary introductory expressions.

Avoid:

- É importante observar que...
- Deve-se notar que...
- Vale ressaltar que...
- Como podemos ver...
- Convém mencionar que...

when the information can be stated directly.

Instead of:

> É importante observar que este método requer uma senha.

Prefer:

> Este método requer uma senha.

---

## 4. Addressing the reader

Use direct instructions without explicit pronouns.

Good:

- Abra o arquivo.
- Configure as opções.
- Salve o documento.

Avoid:

- Você deve abrir o arquivo.
- Você precisa configurar as opções.
- O usuário deve salvar o documento.

Use `você` only when the pronoun itself is necessary for clarity or contrast.

---

## 5. Headings

Use sentence-style capitalization.

Good:

- Converter PDF para DOCX
- Criar um documento PDF
- Extrair texto de um PDF
- Configurar as opções de conversão
- Trabalhar com formulários PDF

Bad:

- Converter PDF Para DOCX
- Criar Um Documento PDF
- Extrair Texto De Um PDF
- Trabalhar Com Formulários PDF

Capitalize only:

- the first word;
- proper names;
- product names;
- technologies;
- identifiers whose official spelling requires capitalization.

Do not normally add a period at the end of a heading.

Good:

> Criar um documento PDF

Bad:

> Criar um documento PDF.

---

## 6. Task headings

Use the infinitive for headings describing tasks or operations.

Good:

- Criar um documento PDF
- Adicionar uma página
- Converter PDF para DOCX
- Extrair imagens
- Configurar opções de conversão
- Salvar o documento

Avoid mixing grammatical structures among sibling headings.

Bad:

- Criação de um documento
- Adicionar uma página
- Como configurar fontes
- Salvamento do documento

Prefer:

- Criar um documento
- Adicionar uma página
- Configurar fontes
- Salvar o documento

---

## 7. Conceptual headings

Use concise noun phrases for conceptual and reference sections.

Good:

- Pré-requisitos
- Opções de conversão
- Formatos compatíveis
- Limitações conhecidas
- Gerenciamento de fontes
- Estrutura do documento
- Referência da API
- Configurações avançadas

Do not convert conceptual headings into infinitives merely because the section discusses an operation.

---

## 8. Step-by-step instructions

Use direct imperative forms.

Good:

- Crie um objeto `Document`.
- Abra o arquivo PDF.
- Adicione uma página ao documento.
- Configure as opções de conversão.
- Salve o documento.

Bad:

- Criar um objeto `Document`.
- Abrir o arquivo PDF.
- Adicionar uma página.
- Configurar as opções.
- Salvar o documento.

Avoid unnecessarily impersonal constructions.

Avoid:

- Deve-se criar um objeto `Document`.
- Um objeto `Document` deve ser criado.
- É necessário criar um objeto `Document`.

Prefer:

- Crie um objeto `Document`.

---

## 9. Common imperative forms

Normalize common procedural verbs as follows:

| Infinitive | Preferred instruction |
|---|---|
| acessar | Acesse |
| adicionar | Adicione |
| abrir | Abra |
| baixar | Baixe |
| chamar | Chame |
| configurar | Configure |
| converter | Converta |
| copiar | Copie |
| criar | Crie |
| definir | Defina |
| excluir | Exclua |
| executar | Execute |
| exportar | Exporte |
| extrair | Extraia |
| importar | Importe |
| instalar | Instale |
| obter | Obtenha |
| salvar | Salve |
| selecionar | Selecione |
| especificar | Especifique |
| usar | Use |
| verificar | Verifique |

Follow the approved glossary when it specifies another verb.

Prefer concise verbs.

Use:

> Use

rather than unnecessarily formal:

> Utilize

unless `utilizar` is established by the project's terminology.

---

## 10. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. Crie um objeto `Document`.
2. Adicione uma página ao documento.
3. Crie um objeto `TextFragment`.
4. Adicione o texto à página.
5. Salve o documento PDF.

Each numbered item should normally represent one primary action.

Avoid:

> 1. Crie o documento, adicione uma página, configure a fonte, adicione o texto e salve o arquivo.

Split meaningful actions into separate steps.

Closely related operations may remain together when splitting them would make the procedure unnecessarily fragmented.

---

## 11. Complete sentences in steps

Write procedural steps as complete sentences.

Begin with a capital letter and end with appropriate punctuation.

Good:

1. Abra o documento PDF.
2. Selecione a página que deseja processar.
3. Extraia o texto da página.

Bad:

1. abrir documento
2. seleção da página
3. extrair texto

---

## 12. Context before action

When useful, establish where the action occurs before stating the action.

Good:

- No menu **Arquivo**, selecione **Salvar como**.
- Em `PdfSaveOptions`, defina a propriedade `Compliance`.
- No Visual Studio, abra o **Gerenciador de Pacotes NuGet**.
- Na página **Configurações**, ative a opção **Modo avançado**.

Use the exact terminology of the documented UI.

---

## 13. One primary action per step

Prefer one primary action per numbered step.

Good:

1. Crie um objeto `Document`.
2. Adicione uma página.
3. Salve o documento.

Closely related operations may be combined.

Acceptable:

> Crie um objeto `Document` e passe o caminho do arquivo para o construtor.

Do not split every API call into its own step when the calls form one logical action.

---

## 14. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. Crie um objeto `Document`.

   Esse objeto representa o documento PDF que será processado.

The numbered sentence describes the action.

The paragraph below it explains the action, object, or result.

---

## 15. Figure captions

Use:

`Figura N. Descrição`

Examples:

- Figura 1. Estrutura do documento PDF
- Figura 2. Opções de conversão
- Figura 3. Resultado da conversão
- Figura 4. Configuração do projeto

Use sentence-style capitalization.

Keep captions concise.

Good:

> Figura 5. Resultado da extração de texto

Avoid:

> Figura 5. Resultado Da Extração De Texto

Avoid generic captions:

> Figura 5. Captura de tela

> Figura 5. Imagem

> Figura 5. Exemplo

Describe what the figure actually communicates.

---

## 16. Referencing figures

In running text, use:

- Consulte a figura 2.
- A figura 3 mostra o resultado da conversão.
- A configuração do projeto é mostrada na figura 4.

Use lowercase `figura` in ordinary running text unless the publishing system defines another convention.

---

## 17. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- source-code variables;
- package names;
- command-line options;
- file extensions.

Good:

- Crie um objeto `Document`.
- Chame o método `save()`.
- Defina a propriedade `page_info`.
- Use a classe `PdfSaveOptions`.

Bad:

- Crie um objeto `Documento`.
- Chame o método `salvar()`.
- Defina a propriedade `informacoes_pagina`.

Use inline code formatting for identifiers.

---

## 18. Grammar around API identifiers

Apply normal Brazilian Portuguese grammar around technical identifiers.

Good:

- Crie uma instância de `Document`.
- Use o método `save()`.
- Defina a propriedade `Compliance`.
- Acesse a coleção `pages`.
- Passe o objeto para `convert()`.

Do not alter an identifier to make it conform to Portuguese morphology.

---

## 19. Files, paths, commands, and values

Format literal filenames, paths, commands, extensions, and literal values as code.

Good:

- Abra `input.pdf`.
- Salve o resultado como `output.pdf`.
- Execute `dotnet build`.
- Abra o diretório `C:\Samples\PDF`.
- Defina o valor como `true`.

Do not translate literal values.

---

## 20. UI terminology

Preserve the exact text displayed by the documented product.

If the Brazilian Portuguese UI displays:

> **Salvar como**

write:

> Selecione **Salvar como**.

If the actual product displays:

> **Save As**

write:

> Selecione **Save As**.

Do not invent translated UI labels.

Do not replace a pt-BR product label with a pt-PT equivalent.

---

## 21. Preferred Brazilian technical terminology

Use established Brazilian technical terminology consistently.

Preferred examples:

| Concept | Preferred pt-BR |
|---|---|
| file | arquivo |
| user | usuário |
| screen | tela |
| source code | código-fonte |
| database | banco de dados |
| directory | diretório |
| folder | pasta |
| application | aplicativo / aplicação according to context |
| settings | configurações |
| library | biblioteca |
| method | método |
| property | propriedade |
| parameter | parâmetro |
| interface | interface |
| user interface | interface do usuário |
| package | pacote |
| framework | framework |
| runtime | runtime / ambiente de execução according to glossary |
| server | servidor |
| client | cliente |
| browser | navegador |

The approved project glossary takes precedence.

---

## 22. Avoid European Portuguese forms

When reviewing pt-BR documentation, flag unintended pt-PT terminology.

Typical examples:

| Avoid in pt-BR | Prefer |
|---|---|
| ficheiro | arquivo |
| utilizador | usuário |
| ecrã | tela |
| rato | mouse |
| guardar o arquivo | salvar o arquivo |
| descarregar | baixar / fazer download |
| gestor de pacotes | gerenciador de pacotes |

Do not change literal UI labels, quotations, API identifiers, or product terminology even if they contain a different regional form.

---

## 23. English technical terms

Translate established concepts when natural Brazilian Portuguese terminology exists.

Good:

- código-fonte
- banco de dados
- interface do usuário
- arquivo
- configurações

Preserve established technology and product names:

- .NET
- Python
- Java
- JSON
- REST API
- NuGet
- GitHub

Avoid unnecessary English verbs.

Bad:

> Faça um save do documento.

Prefer:

> Salve o documento.

But preserve an actual API identifier:

> Chame o método `save()`.

---

## 24. Download and upload terminology

Follow the approved glossary first.

For general Brazilian developer documentation, acceptable forms include:

- baixar;
- fazer download;
- carregar;
- fazer upload.

Prefer concise natural Portuguese when there is no established product term.

Example:

> Baixe o arquivo.

However, preserve UI labels such as **Download** or **Upload** when those are the actual labels displayed by the product.

Do not use pt-PT `descarregar` for ordinary pt-BR instructions.

---

## 25. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate among:

- arquivo / ficheiro;
- usuário / utilizador;
- tela / ecrã;
- salvar / guardar;
- usar / utilizar;
- excluir / apagar / remover;
- diretório / pasta when they refer to the same concept.

Different terms are acceptable when they represent genuinely different concepts.

Example:

`diretório` may describe a filesystem directory while `pasta` may be the actual UI terminology.

The approved glossary takes precedence.

---

## 26. Notes, tips, and warnings

Use consistent labels.

Recommended:

> **Observação:** informação complementar.

> **Dica:** orientação opcional ou abordagem mais eficiente.

> **Importante:** informação necessária para concluir a tarefa corretamente.

> **Aviso:** risco, operação destrutiva, problema de segurança ou possível perda de dados.

If the project's terminology uses **Nota** or **Advertência**, preserve that convention consistently.

Do not alternate labels without a semantic reason.

---

## 27. Macros and placeholders

Never translate or modify macros and placeholders unless explicitly instructed.

Examples:

- `{{productName}}`
- `{{language}}`
- `{0}`
- `{filename}`
- `%PATH%`
- `${HOME}`

Good:

> Instale o pacote `{{productName}}`.

Bad:

> Instale o pacote `{{nomeDoProduto}}`.

Preserve placeholder spelling, capitalization, braces, and delimiters exactly.

---

## 28. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- Criar um documento
- Adicionar uma página
- Configurar fontes
- Salvar o documento

Bad:

- Criar um documento
- Adição de uma página
- Como configurar fontes
- Salvamento do documento

Keep procedural instructions parallel:

- Crie...
- Adicione...
- Configure...
- Salve...

---

## 29. Normalization examples

### Heading capitalization

Before:

> Criar Um Documento PDF.

After:

> Criar um documento PDF

### Instruction

Before:

> Criar um objeto `Document`.

After:

> Crie um objeto `Document`.

### Impersonal instruction

Before:

> Deve-se salvar o documento.

After:

> Salve o documento.

### European Portuguese terminology

Before:

> Abra o ficheiro e guarde o resultado.

After:

> Abra o arquivo e salve o resultado.

### Figure caption

Before:

> Figure 2: Conversion Result

After:

> Figura 2. Resultado da conversão

### API identifier

Incorrect:

> Chame o método `salvar()`.

Correct:

> Chame o método `save()`.

Only make this correction when `save()` is the actual API identifier.

### UI label

If the actual UI says **Save As**, do not change:

> Selecione **Save As**.

to:

> Selecione **Salvar como**.

---

## 30. Agent decision order

When reviewing Brazilian Portuguese documentation:

1. Determine the structural role of the text.
2. Preserve API identifiers, commands, paths, macros, filenames, and actual UI labels.
3. Verify that the text uses Brazilian Portuguese rather than European Portuguese.
4. Determine whether a heading describes a task or concept.
5. Use infinitives for task headings.
6. Use noun phrases for conceptual headings.
7. Use direct imperatives for procedural steps.
8. Apply sentence-style capitalization.
9. Preserve parallel grammatical structure.
10. Apply the approved pt-BR glossary.
11. Check figure-caption formatting.
12. Check punctuation and technical formatting.
13. Check for unintended English verbs or unnecessary Anglicisms.
14. Verify that technical literals were not translated.

Never normalize documentation mechanically without first determining context.

---

## 31. Review checklist

Before completing a Brazilian Portuguese technical-documentation task, verify:

- [ ] The target locale is `pt-BR`.
- [ ] No unintended pt-PT terminology remains.
- [ ] `arquivo`, not `ficheiro`, is used for ordinary files.
- [ ] `usuário`, not `utilizador`, is used for users.
- [ ] `tela`, not `ecrã`, is used for screens.
- [ ] `salvar`, not `guardar`, is used for saving files unless product terminology requires otherwise.
- [ ] Task headings use infinitives.
- [ ] Conceptual headings use appropriate noun phrases.
- [ ] Headings use sentence-style capitalization.
- [ ] Headings do not end with unnecessary periods.
- [ ] Procedural steps use direct imperative forms.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel structures.
- [ ] Figure captions follow `Figura N. Descrição`.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, paths, macros, and placeholders remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Technical terminology is consistent.
- [ ] The approved pt-BR glossary takes precedence.

## Core rule

**Use Brazilian Portuguese consistently: infinitives for task headings, direct imperatives for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> Criar um documento PDF

Step:

> Crie um objeto `Document`.

Figure:

> Figura 1. Estrutura do documento PDF

Locale:

> `pt-BR`