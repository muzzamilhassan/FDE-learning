# In JS: const tags = new Set(["python", "js", "python"]);
tags = {"python", "javascript", "python"}  # Duplicates removed automatically
print("Set:", tags)

# In JS: tags.add("docker"), tags.delete("js"), tags.has("python")
tags.add("docker")
tags.discard("javascript")
print("Is 'python' in tags?:", "python" in tags)

# Set Math Operations (In JS: requires manual filter/spread)
frontend = {"html", "css", "javascript"}
backend = {"python", "javascript", "sql"}

print("Union (|):", frontend | backend)              # All skills
print("Intersection (&):", frontend & backend)      # Common skills
print("Difference (-):", frontend - backend)        # Frontend only
