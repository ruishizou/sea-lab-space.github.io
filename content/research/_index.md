---
# Page title
title: Research Focus
# Page type - we want a landing page (such as a homepage)
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: markdown
    content:
      title: Research Direction
      text: |
        SEA Lab mainly focuses on two groups of people: (i) **general populations**, including end-users and patients, to promote health and well-being, and (ii) **health experts**, including physicians, nurses, and other healthcare providers, to support improved decision-making.
        
        Targeting at these two user groups, the mission of SEA Lab includes three core areas:

    design:
      columns: '1'
      css_class: section-title-left-aligned
      
  - block: markdown
    content:
      title: 1 - Reliable Multimodal Health Insights and Prediction Models
      subtitle: ''
      text: We leverage data from everyday sensors (smartphones, wearables, IoT, social media, to name just a few) and medical records to extract novel behavior insights and develop reliable AI/ML models for health prediction. This supports both general population and health experts.
    design:
      css_class: section-custom-header

  - block: collection
    content:
      title:
      subtitle:
      text: 

      # Display content from the `content/publication/` folder
      filters:
        folders:
          - publication
        tag: 'health prediction'
      
      count: 3

    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      # Choose your content listing view - here we use the `showcase` view
      view: compact
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: false


  - block: markdown
    content:
      title: 2 - Intelligent Interaction and Intervention Techniques
      subtitle: ''
      text: Building on predictive models, we further design and develop human-AI interaction and behavior change intervention techniques that are aimed at promoting health and well-being. This area mainly focuses on general populations.
    design:
      css_class: section-custom-header

  - block: collection
    content:
      title:
      subtitle:
      text: 
      # Display content from the `content/publication/` folder
      filters:
        folders:
          - publication
        tag: 'intelligent interaction and intervention'
      count: 3

    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      # Choose your content listing view - here we use the `showcase` view
      view: compact
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: false

  - block: markdown
    content:
      title: 3 - AI-Powered Clinical Decision Support
      subtitle: ''
      text: We integrate AI models into clinical decision support systems, enabling health experts to interpret actionable insights, collaborate with AI, and make more informed decisions. This area is experts-focused.
    design:
      css_class: section-custom-header

  - block: collection
    content:
      title:
      subtitle:
      text: 

      # Display content from the `content/publication/` folder
      filters:
        folders:
          - publication
        tag: 'clinical support'

      count: 3

    design:
      # Choose how many columns the section has. Valid values: '1' or '2'.
      columns: '1'
      # Choose your content listing view - here we use the `showcase` view
      view: compact
      # For the Showcase view, do you want to flip alternate rows?
      flip_alt_rows: false


---
