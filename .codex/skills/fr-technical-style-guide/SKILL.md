---
name: fr-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing French programming documentation. It normalizes headings, step-by-step instructions, figure captions, terminology, API identifiers, UI labels, punctuation, and technical formatting to consistent technical French.
---

# French Technical Documentation Style

## Goal

Normalize French programming documentation to a clear, concise, consistent style suitable for developers.

Use **neutral international French** unless project-specific localization instructions specify a regional convention.

Address the reader using **vous** in procedural instructions.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General French writing conventions.

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

Do not normalize text mechanically without first determining its role.

---

## 2. General writing style

Use concise, direct technical French.

Prefer short sentences and active constructions.

Good:

- Cette méthode enregistre le document PDF.
- L'exemple suivant convertit un fichier PDF au format DOCX.

Avoid unnecessarily verbose constructions.

Avoid:

- Il convient de noter que cette méthode permet d'effectuer l'enregistrement du document.

Prefer:

- Cette méthode enregistre le document.

Avoid unnecessary introductory expressions such as:

- Il convient de noter que...
- Il est important de noter que...
- Comme nous pouvons le voir...
- On peut remarquer que...

State the information directly whenever possible.

---

## 3. Headings

Use sentence-style capitalization.

Good:

- Convertir un PDF en DOCX
- Créer un document PDF
- Extraire le texte d'un PDF
- Configurer les options de conversion
- Options de conversion

Bad:

- Convertir Un PDF En DOCX
- Créer Un Document PDF
- Extraire Le Texte D'Un PDF

Capitalize only the first word and words that independently require capitalization, such as proper names, technologies, products, and identifiers.

Do not normally place a period at the end of a heading.

Good:

- Créer un document PDF

Bad:

- Créer un document PDF.

---

## 4. Task headings

Use the infinitive for headings describing an operation or procedure.

Good:

- Créer un document PDF
- Ajouter une page
- Convertir un PDF en DOCX
- Extraire des images
- Configurer les options
- Enregistrer le document

Avoid mixing grammatical structures among sibling headings.

Bad:

- Création d'un document
- Ajouter une page
- Comment configurer les polices
- Enregistrement du document

Prefer:

- Créer un document
- Ajouter une page
- Configurer les polices
- Enregistrer le document

---

## 5. Conceptual headings

Use concise noun phrases for conceptual and reference sections.

Good:

- Prérequis
- Options de conversion
- Formats pris en charge
- Limitations connues
- Gestion des polices
- Structure du document
- Référence de l'API

Do not convert a conceptual heading into an infinitive merely because the section discusses an operation.

---

## 6. Step-by-step instructions

Use the **vous imperative** for explicit procedural steps.

Good:

- Créez un objet `Document`.
- Ouvrez le fichier PDF.
- Ajoutez une page au document.
- Configurez les options de conversion.
- Enregistrez le document.

Avoid infinitive instructions in ordinary step-by-step procedures.

Bad:

- Créer un objet `Document`.
- Ouvrir le fichier PDF.
- Ajouter une page.
- Configurer les options.
- Enregistrer le document.

Also avoid unnecessarily impersonal instructions.

Avoid:

- Il faut créer un objet `Document`.
- Un objet `Document` doit être créé.

Prefer:

- Créez un objet `Document`.

---

## 7. Common instruction normalization

Normalize common procedural verbs as follows:

| Infinitive | Instruction |
|---|---|
| ajouter | Ajoutez |
| appeler | Appelez |
| configurer | Configurez |
| convertir | Convertissez |
| copier | Copiez |
| créer | Créez |
| définir | Définissez |
| enregistrer | Enregistrez |
| exécuter | Exécutez |
| exporter | Exportez |
| extraire | Extrayez |
| importer | Importez |
| installer | Installez |
| ouvrir | Ouvrez |
| obtenir | Obtenez |
| saisir | Saisissez |
| sélectionner | Sélectionnez |
| spécifier | Spécifiez |
| supprimer | Supprimez |
| télécharger | Téléchargez |
| utiliser | Utilisez |
| vérifier | Vérifiez |

Follow the approved glossary if it establishes another preferred verb.

Do not alternate unnecessarily between synonyms such as:

- utiliser;
- employer;
- se servir de.

For developer documentation, prefer **utiliser** unless project terminology specifies otherwise.

---

## 8. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. Créez un objet `Document`.
2. Ajoutez une page au document.
3. Créez un objet `TextFragment`.
4. Ajoutez le texte à la page.
5. Enregistrez le document PDF.

Each step should normally contain one primary action.

Avoid combining an entire procedure into one step.

Bad:

1. Créez le document, ajoutez une page, configurez la police, ajoutez le texte et enregistrez le fichier.

Split meaningful stages into separate steps.

Closely related actions may remain together when separating them would make the procedure unnecessarily fragmented.

---

## 9. Step punctuation

Write procedural steps as complete sentences.

Start each step with a capital letter and end it with appropriate punctuation.

Good:

1. Ouvrez le document PDF.
2. Sélectionnez la page à traiter.
3. Extrayez le texte de la page.

Bad:

1. ouvrir le document
2. sélection de la page
3. extraction du texte

---

## 10. Context before action

When the location or object of an action matters, provide the context clearly.

Good:

- Dans le menu **Fichier**, sélectionnez **Enregistrer sous**.
- Dans `PdfSaveOptions`, définissez la propriété `Compliance`.
- Dans Visual Studio, ouvrez le **Gestionnaire de packages NuGet**.

Do not make the reader infer where the action should be performed.

---

## 11. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. Créez un objet `Document`.

   Cet objet représente le document PDF à traiter.

The numbered sentence describes the action.

The following paragraph explains the action or its result.

---

## 12. Figure captions

Use the following default pattern:

`Figure N. Description`

Examples:

- Figure 1. Structure du document PDF
- Figure 2. Options de conversion
- Figure 3. Résultat de la conversion
- Figure 4. Configuration du projet

Use sentence-style capitalization.

Keep captions concise and descriptive.

Avoid:

- Figure 3. Résultat De La Conversion
- Figure 3. Capture d'écran
- Figure 3. Exemple

Describe what the figure actually communicates.

---

## 13. Figure references

In running text, use:

- Consultez la figure 2.
- La figure 3 montre le résultat de la conversion.
- La configuration du projet est présentée dans la figure 4.

Use lowercase `figure` in ordinary running text unless the project's publishing system specifies another convention.

---

## 14. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- variables in source code;
- package names;
- command-line options;
- file extensions.

Good:

- Créez un objet `Document`.
- Appelez la méthode `save()`.
- Définissez la propriété `page_info`.

Bad:

- Créez un objet `DocumentPDF`.
- Appelez la méthode `enregistrer()`.

Use code formatting for identifiers.

---

## 15. Articles and API identifiers

Apply normal French grammar around API identifiers.

Good:

- Créez une instance de `Document`.
- Utilisez la méthode `save()`.
- Définissez la propriété `Compliance`.
- Accédez à la collection `pages`.

Do not alter an identifier to make it conform to French grammar.

---

## 16. Files, paths, and commands

Format literal filenames, paths, commands, and extensions as code.

Good:

- Ouvrez `input.pdf`.
- Enregistrez le résultat dans `output.pdf`.
- Exécutez `dotnet build`.
- Ouvrez le répertoire `C:\Samples\PDF`.

Do not translate literal values.

---

## 17. UI labels

Preserve the exact text displayed by the documented product.

If the French UI displays:

**Enregistrer sous**

write:

- Sélectionnez **Enregistrer sous**.

If the product displays:

**Save As**

write:

- Sélectionnez **Save As**.

Do not invent localized UI labels.

---

## 18. Technical terminology

Prefer established French technical terminology when a natural and widely understood term exists.

Examples:

- fichier
- répertoire
- code source
- base de données
- configuration
- interface utilisateur
- bibliothèque
- méthode
- propriété
- paramètre

Preserve technologies, product names, formats, and API terminology:

- .NET
- Python
- Java
- REST API
- JSON
- NuGet
- GitHub

Avoid unnecessary mixtures of French and English.

Avoid:

- Faites un save du document.

Prefer:

- Enregistrez le document.

But preserve actual API identifiers:

- Appelez la méthode `save()`.

---

## 19. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate between terms such as:

- fichier / document, when they represent the same object;
- répertoire / dossier;
- utiliser / employer;
- supprimer / effacer;
- sélectionner / choisir.

Use different terms when they genuinely represent different concepts.

The approved project glossary takes precedence.

---

## 20. Notes and warnings

Use consistent labels.

Recommended:

- **Remarque :** supplementary information.
- **Conseil :** optional advice.
- **Important :** information necessary for successful completion.
- **Avertissement :** potential risk, destructive action, security issue, or data loss.

Use the required French spacing before the colon according to the project's typography rules.

Do not alternate labels without a semantic reason.

---

## 21. French punctuation

Apply French punctuation consistently in prose.

Use the project's typography conventions for spaces before punctuation such as:

- `:`
- `;`
- `?`
- `!`

Do not modify punctuation inside:

- source code;
- API identifiers;
- commands;
- URLs;
- literal UI labels;
- filenames.

Project-specific typography rules take precedence over generic French conventions.

---

## 22. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- Créer un document
- Ajouter une page
- Configurer les polices
- Enregistrer le document

Bad:

- Créer un document
- Ajout d'une page
- Comment configurer les polices
- Enregistrement du document

Keep procedural steps parallel as well:

- Créez...
- Ajoutez...
- Configurez...
- Enregistrez...

---

## 23. Normalization examples

### Heading

Before:

`Création D'Un Document PDF.`

After:

`Créer un document PDF`

### Instruction

Before:

`Créer un objet Document.`

After:

`Créez un objet `Document`.`

### Impersonal instruction

Before:

`Il faut enregistrer le document.`

After:

`Enregistrez le document.`

### Figure

Before:

`Figure 2: Conversion Result`

After:

`Figure 2. Résultat de la conversion`

### API identifier

Before:

`Appelez la méthode enregistrer().`

After:

`Appelez la méthode `save()`.`

Only perform the last transformation when `save()` is the actual API identifier.

---

## 24. Review checklist

Before completing a French technical-documentation task, verify:

- [ ] Task headings use infinitives.
- [ ] Conceptual headings use appropriate noun phrases.
- [ ] Headings use sentence-style capitalization.
- [ ] Headings do not end with unnecessary periods.
- [ ] Procedural steps use the `vous` imperative.
- [ ] Steps are complete sentences.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel grammatical structures.
- [ ] Figure captions follow `Figure N. Description`.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, and paths remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Technical terminology is consistent.
- [ ] French punctuation follows project conventions.
- [ ] The approved glossary takes precedence over generic terminology.

## Core rule

**Use infinitives for task headings, the `vous` imperative for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> Créer un document PDF

Step:

> Créez un objet `Document`.

Figure:

> Figure 1. Structure du document PDF