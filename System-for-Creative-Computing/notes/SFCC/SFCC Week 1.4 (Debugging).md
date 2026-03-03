## 📌 What is Debugging?  

Debugging = finding and fixing errors (bugs) in a program.  
  
It often takes **longer than writing the code**.  
  
---  

## 🧠 Debugging Mindset  

- Stay calm  
- Don’t randomly change things  
- Change **one thing at a time**  
- Think logically, not emotionally  
  
---  
## 🔄 Basic Debugging Steps  
  
### 1️⃣ Reproduce the Bug  

- Can you make it happen again?  
- What inputs cause it?  
  
> If you can’t reproduce it, it’s hard to fix.  

---
### 2️⃣ Read the Error Message  

- Look at the exact line mentioned  
- Check stack traces  
- Don’t ignore warnings  

---
### 3️⃣ Think Backwards  

- What caused this result?  
- What changed recently?  
- What values are wrong?  
  
---  
  
### 4️⃣ Use Print / Logging  

Add temporary prints:  
```python  
print(variable_name)
```

Check:
- Are variables what you expect?
- Is the code running in the order you think?

---
### 5️⃣ Use a Debugger (if available)

- Set breakpoints
- Step through line by line
- Inspect variables

---

## 🔍 Helpful Techniques

### Divide and Conquer

- Comment out half the code
- Narrow down where the problem starts
- Reduce to the smallest example that still fails

### Compare Working vs Broken

- What’s different?
- Use version control (like Git) to check changes

---

## 🧪 Common Bug Types

- Wrong variable value
- Logic error (condition wrong)
- Off-by-one errors
- Wrong comparison (`=` vs `==`)
- Not handling edge cases

---

## 🛠 Good Habits

- Fix bugs early
- Write clear code
- Add comments
- Use assertions when possible
- Keep notes of what you tried

---

## ⚡ Quick Debug Checklist

When stuck, ask:

- What is happening?
- What *should* be happening?
- Where do they start being different?
- What changed recently?
- What assumptions am I making?
