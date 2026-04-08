# Layout Tutorial: From Basic Structure to Responsive Design

## Goal
In this task, you will take a very plain webpage and slowly improve it into a better layout.

You will learn how to:
- organise content
- style sections
- use Flexbox
- use Grid
- make the page responsive with media queries

Use only:
- HTML
- Internal CSS

---

# Step 1: Look at the starter file

Open the HTML file in Visual Studio Code and run it in the browser.

You should notice:
- the page looks plain
- everything is stacked on top of each other
- the boxes do not form a proper layout
- the page does not feel modern
- the page is not responsive in a useful way

Your job is to improve this step by step.

---

# Step 2: Improve the body

Start with the `body` selector.

## What to change
Try improving:
- font-family
- background-color
- text color
- margin
- line-height

## Example ideas
- Choose a cleaner font
- Use a softer background colour instead of plain white
- Make text easier to read

## Focus
This step improves the whole look of the page before changing the layout.

---

# Step 3: Improve the main sections

Now style:
- `header`
- `nav`
- `main`
- `footer`

## What to change
Try adding:
- better padding
- better margins
- max-width
- border-radius
- box-shadow
- better background colours

## Goal
Make each section look like part of the same website.

## Hint
A website usually looks better when content does not stretch too wide across the whole screen.

Example idea:
- center the page with `max-width`
- use `margin: 20px auto;`

---

# Step 4: Improve the navigation

At the moment, the navigation is just plain text.

## Your task
Turn it into a proper menu.

## Step-by-step
1. Put each menu item on its own line in the HTML, or wrap them in separate elements such as:
   - `<a>`
   - `<span>`
   - `<div>`

2. Style the navigation with CSS

3. Use **Flexbox** to line items up

## CSS ideas
You may want to use:
```css
nav {
  display: flex;
  gap: 20px;
}
```

## Then improve further
- add spacing
- remove default link underline if you use links
- add hover effects
- align items neatly

## Goal
Create a clean horizontal navigation bar.

---

# Step 5: Improve the first section

The first section is the main content area.

## Your task
Turn it into a stronger introduction section.

## You can:
- make the heading larger
- improve paragraph spacing
- add a button
- add more white space
- change background colour

## Goal
Make this section feel like the main focus of the page.

This is sometimes called a **hero section**.

---

# Step 6: Turn the boxes into a layout

Right now, the boxes sit underneath each other.

You will now learn your first real layout method.

## Option A: Use Flexbox

Apply Flexbox to the parent area that contains the boxes.

For example:
```css
section {
}
```

You should not apply Flexbox to every section on the page.
Instead, add a class in the HTML to the section that contains the boxes.

Example:
```html
<section class="cards-section">
```

Then in CSS:
```css
.cards-section {
  display: flex;
  gap: 20px;
}
```

## What this does
- `display: flex;` puts items in a row
- `gap` adds space between them

## Problem to solve
The boxes may not all size evenly.

Try adding this to the boxes:
```css
.box {
  flex: 1;
}
```

## Goal
Make 3 equal cards in a row.

---

# Step 7: Make the boxes look better

Now improve the `.box` style.

## Try adding
- padding
- border-radius
- background-color
- box-shadow
- bigger headings
- more spacing between text elements

## Goal
Make each box look like a proper card.

---

# Step 8: Try Grid instead of Flexbox

Now test another layout system.

Flexbox is very good for rows or columns.
Grid is very good for structured layouts.

Change the container of the boxes from Flexbox to Grid.

## Example
```css
.cards-section {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}
```

## What this means
- `display: grid;` turns the section into a grid
- `grid-template-columns: 1fr 1fr 1fr;` creates 3 equal columns

## Compare
Ask yourself:
- Which was easier, Flexbox or Grid?
- Which gives more control?

## Goal
Understand both layout methods.

---

# Step 9: Add width control to the page

A good webpage often keeps content inside a container.

## Your task
Add a wrapper or use existing sections so the website does not become too wide.

## You can use
```css
main,
header,
nav,
footer {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}
```

## Goal
Create a cleaner desktop layout.

---

# Step 10: Make the design more consistent

Now improve the visual design.

## Look for consistency in:
- colours
- font sizes
- spacing
- border radius
- shadows

## Good design questions
- Do all sections feel like they belong together?
- Is spacing consistent?
- Are headings clearly larger than normal text?
- Is the page easy to read?

---

# Step 11: Make the page responsive

Now check the page on a small screen.

In the browser, make the window smaller.

## What problems do you notice?
Common problems:
- boxes become too narrow
- navigation gets cramped
- text may look too large or too small
- spacing may stop working well

---

# Step 12: Add your first media query

A media query lets you change the layout on smaller screens.

## Example
```css
@media (max-width: 700px) {
  .cards-section {
    grid-template-columns: 1fr;
  }
}
```

## What this does
- when the screen is 700px wide or smaller
- the 3-column grid becomes 1 column
- the boxes stack vertically

## Goal
Make the content easier to read on phones.

---

# Step 13: Make the navigation responsive

The navigation also needs to work on smaller screens.

## If using Flexbox
Try changing direction inside a media query:

```css
@media (max-width: 700px) {
  nav {
    flex-direction: column;
  }
}
```

## Goal
Make the menu easier to use on mobile.

---

# Step 14: Improve spacing for small screens

Responsive design is not only about stacking items.

You should also check:
- padding
- font size
- gaps between elements

## Example ideas
Inside your media query, you might reduce:
- padding
- gap size
- heading size

## Goal
Make the page feel comfortable on mobile, not crowded.

---

# Step 15: Final checks

Before you finish, check:

## Desktop
- Does the page look balanced?
- Are sections aligned well?
- Are the cards arranged properly?

## Mobile
- Do the boxes stack properly?
- Is the menu usable?
- Is text still easy to read?
- Does anything overflow off the page?

---

# Suggested Build Order

Use this order while working:
1. body
2. main sections
3. navigation
4. first content section
5. box/card layout with Flexbox
6. box/card layout with Grid
7. better styling
8. max-width and alignment
9. media query
10. mobile improvements

---

# Mini Reference

## Flexbox
Use for:
- nav bars
- rows of cards
- aligning items horizontally or vertically

Useful properties:
```css
display: flex;
gap: 20px;
justify-content: space-between;
align-items: center;
flex: 1;
flex-direction: column;
```

## Grid
Use for:
- card layouts
- rows and columns
- more structured layouts

Useful properties:
```css
display: grid;
grid-template-columns: 1fr 1fr 1fr;
gap: 20px;
```

## Media Query
Use for:
- changing layout on smaller screens

Example:
```css
@media (max-width: 700px) {
  .cards-section {
    grid-template-columns: 1fr;
  }
}
```

---

# Extension Tasks
When you finish, try one or more of these:
- add a button with hover effect
- change the website into a real theme such as travel, food, school, or gaming
- add images
- make the footer more detailed
- create a tablet layout as well as a mobile layout
- create a colour palette using CSS variables

---

# Success Criteria
A strong result should:
- show clear improvement from the starter file
- use layout techniques correctly
- use either Flexbox or Grid well
- include a responsive design
- look clean and organised
- work on both desktop and mobile
