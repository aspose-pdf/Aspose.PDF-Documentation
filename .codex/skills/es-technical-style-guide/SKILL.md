---
name: es-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Spanish programming documentation. It normalizes headings, numbered instructions, figure captions, terminology, API identifiers, and technical formatting to consistent neutral Spanish.
---

# Spanish Technical Documentation Style

## Goal

Normalize Spanish programming documentation to a clear, consistent, action-oriented technical style suitable for developers.

Use **neutral international Spanish** unless a project-specific localization guide says otherwise.

## Priority

When rules conflict, apply them in this order:

1. Project-specific terminology or localization instructions.
2. Approved glossary.
3. Product and API terminology.
4. This style guide.
5. General Spanish writing conventions.

Never change API identifiers, commands, paths, filenames, or actual UI labels merely to satisfy a linguistic rule.

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

Do not apply transformations mechanically without determining the text's role.

---

## 2. Headings

Use sentence-style capitalization.

Good:

- Convertir PDF a DOCX
- Crear un documento PDF
- Extraer texto de un PDF
- Configurar las opciones de conversión
- Opciones de conversión

Bad:

- Convertir PDF A DOCX
- Crear Un Documento PDF
- Extraer Texto De Un PDF

Do not normally add a period at the end.

Good:

- Crear un documento PDF

Bad:

- Crear un documento PDF.

Preserve capitalization required by proper names, products, technologies, and identifiers.

---

## 3. Task headings

Use the infinitive for headings describing an operation.

Good:

- Crear un documento PDF
- Añadir una página
- Convertir PDF a DOCX
- Extraer imágenes
- Guardar el documento

Avoid mixing grammatical structures among sibling headings.

Bad:

- Creación de un documento
- Añadir una página
- Cómo configurar las fuentes
- Guardado del documento

Prefer:

- Crear un documento
- Añadir una página
- Configurar las fuentes
- Guardar el documento

---

## 4. Conceptual headings

Use noun phrases for conceptual or reference sections.

Good:

- Requisitos previos
- Opciones de conversión
- Formatos compatibles
- Gestión de fuentes
- Limitaciones conocidas
- Estructura del documento

Do not convert a conceptual heading to an infinitive merely because the section discusses an operation.

---

## 5. Step-by-step instructions

Use the formal **usted** imperative for explicit procedural steps.

Good:

- Cree un objeto `Document`.
- Abra el archivo PDF.
- Añada una página.
- Configure las opciones de conversión.
- Guarde el documento.

Bad:

- Crear un objeto `Document`.
- Abrir el archivo PDF.
- Añadir una página.
- Configurar las opciones.
- Guardar el documento.

Also avoid unnecessarily impersonal instructions.

Avoid:

- Se debe crear un objeto `Document`.

Prefer:

- Cree un objeto `Document`.

---

## 6. Common instruction normalization

Normalize common infinitives as follows:

| Avoid | Prefer |
|---|---|
| Abrir | Abra |
| Acceder | Acceda |
| Añadir | Añada |
| Comprobar | Compruebe |
| Configurar | Configure |
| Convertir | Convierta |
| Copiar | Copie |
| Crear | Cree |
| Definir | Defina |
| Descargar | Descargue |
| Ejecutar | Ejecute |
| Eliminar | Elimine |
| Establecer | Establezca |
| Extraer | Extraiga |
| Guardar | Guarde |
| Importar | Importe |
| Instalar | Instale |
| Introducir | Introduzca |
| Llamar | Llame |
| Obtener | Obtenga |
| Seleccionar | Seleccione |
| Especificar | Especifique |
| Utilizar | Utilice |
| Verificar | Verifique |

Follow an approved glossary if it specifies another verb.

---

## 7. Numbered procedures

Use numbered lists when order matters.

Each step should normally contain one primary action.

Good:

1. Cree un objeto `Document`.
2. Añada una página al documento.
3. Configure las opciones de conversión.
4. Guarde el documento.

Avoid combining an entire procedure into one step.

Bad:

1. Cree el documento, añada una página, configure las opciones, conviértalo y guarde el resultado.

Closely related operations may remain together when separating them would make the procedure unnecessarily fragmented.

---

## 8. Step punctuation

Write steps as complete sentences.

Start with a capital letter and end with appropriate punctuation.

Good:

1. Abra el documento PDF.
2. Seleccione la página.
3. Extraiga el texto.

Bad:

1. abrir documento
2. selección de página
3. extraer texto

---

## 9. Context before action

When useful, identify where an action occurs before stating the action.

Good:

- En el menú **Archivo**, seleccione **Guardar como**.
- En `PdfSaveOptions`, establezca la propiedad `Compliance`.
- En Visual Studio, abra el **Administrador de paquetes NuGet**.

---

## 10. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. Cree un objeto `Document`.

   Este objeto representa el documento PDF que se procesará.

The first sentence is the action. The second explains it.

---

## 11. Figure captions

Use:

`Figura N. Descripción`

Examples:

- Figura 1. Estructura del documento PDF
- Figura 2. Opciones de conversión
- Figura 3. Resultado de la conversión

Use sentence-style capitalization.

Avoid:

- Figure 1: Conversion Result
- Figura 1: Resultado De La Conversión
- Figura 1. Captura de pantalla

Prefer a caption that describes what the figure communicates.

---

## 12. Figure references

In running text, use:

- Consulte la figura 2.
- La figura 3 muestra el resultado de la conversión.

Use lowercase `figura` in ordinary running text unless the publishing system defines another convention.

---

## 13. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- code variables;
- package names;
- command-line options;
- file extensions.

Good:

- Cree un objeto `Document`.
- Llame al método `save()`.
- Establezca la propiedad `page_info`.

Bad:

- Cree un objeto `Documento`.
- Llame al método `guardar()`.

Use code formatting for identifiers.

---

## 14. Files, paths, and commands

Format literal filenames, paths, commands, and extensions as code.

Good:

- Abra `input.pdf`.
- Guarde el resultado como `output.pdf`.
- Ejecute `dotnet build`.
- Abra `C:\Samples\PDF`.

Do not translate literal values.

---

## 15. UI labels

Preserve the exact label displayed by the documented product.

If the UI displays:

**Guardar como**

write:

- Seleccione **Guardar como**.

If it displays:

**Save As**

write:

- Seleccione **Save As**.

Do not invent localized UI labels.

---

## 16. Technical terminology

Prefer established Spanish technical terminology when a natural translation exists.

Good:

- archivo
- directorio
- código fuente
- base de datos
- configuración
- interfaz de usuario

Preserve established technologies and product names:

- .NET
- Python
- Java
- REST API
- JSON
- NuGet
- GitHub

Avoid unnecessary Spanglish.

Avoid:

- Haga un save del documento.

Prefer:

- Guarde el documento.

But preserve actual API identifiers:

- Llame al método `save()`.

---

## 17. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate between:

- archivo / fichero;
- carpeta / directorio;
- utilizar / usar / emplear;
- eliminar / borrar;
- seleccionar / elegir.

Follow the approved project glossary when available.

---

## 18. Notes and warnings

Use consistent labels:

- **Nota:** supplementary information.
- **Consejo:** optional advice.
- **Importante:** information necessary for successful completion.
- **Advertencia:** potential risk, destructive action, security issue, or data loss.

Do not alternate labels without a semantic reason.

---

## 19. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- Crear un documento
- Añadir una página
- Configurar las fuentes
- Guardar el documento

Bad:

- Crear un documento
- Adición de páginas
- Cómo configurar las fuentes
- Guardado del documento

Keep procedural steps parallel as well:

- Cree...
- Añada...
- Configure...
- Guarde...

---

## 20. Normalization examples

### Heading

Before:

`Crear Un Documento PDF.`

After:

`Crear un documento PDF`

### Instruction

Before:

`Crear un objeto Document.`

After:

`Cree un objeto `Document`.`

### Impersonal instruction

Before:

`Se debe guardar el documento.`

After:

`Guarde el documento.`

### Figure

Before:

`Figure 2: Conversion Result`

After:

`Figura 2. Resultado de la conversión`

### API identifier

Before:

`Llame al método guardar().`

After:

`Llame al método `save()`.`

Only apply the last transformation when `save()` is the actual API identifier.

---

## 21. Review checklist

Before completing a Spanish technical-documentation task, verify:

- [ ] Task headings use infinitives.
- [ ] Concept headings use appropriate noun phrases.
- [ ] Headings use sentence-style capitalization.
- [ ] Headings do not end with unnecessary periods.
- [ ] Procedural steps use the formal imperative.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel structures.
- [ ] Figure captions follow `Figura N. Descripción`.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, and paths remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Technical terminology is consistent.
- [ ] The approved glossary has priority over generic terminology.

## Core rule

**Use infinitives for task headings, formal imperatives for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> Crear un documento PDF

Step:

> Cree un objeto `Document`.

Figure:

> Figura 1. Estructura del documento PDF