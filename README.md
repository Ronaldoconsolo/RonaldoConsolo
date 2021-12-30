### Hi there This is RonaldoConsolo👋

- 🔭 I’m currently working on learn everything I can
- 🌱 I’m currently learning to code 
- 👯 I’m looking to collaborate on anything to help me learn
- 🤔 I’m looking for help with medical science 
- 💬 Ask me about clinical lab for now
- 📫 How to reach me: ronaldoconsolo@gmail.com
- 😄 Pronouns: he/him
- ⚡ Fun fact: sou Brazilian

<div>
  <a href="https://github.comRonaldoconsolo">
 
name: Generate Datas

on:
  schedule: # execute every 12 hours
    - cron: "* */12 * * *"
  workflow_dispatch:

jobs:
  build:
    name: Jobs to update datas
    runs-on: ubuntu-latest
    steps:
      # Snake Animation
      - uses: Platane/snk@master
        id: snake-gif
        with:
          github_user_name: rafaballerini
          svg_out_path: dist/github-contribution-grid-snake.svg

      - uses: crazy-max/ghaction-github-pages@v2.1.3
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    
