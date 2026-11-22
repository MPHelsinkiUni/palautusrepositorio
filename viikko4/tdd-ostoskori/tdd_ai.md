Did the agent end up with a good implementation and high-quality tests?
- Yes and no. Test-driven development and strict restrictions due to Copilot's tendency to overreach meant that multiple times we had to redo or rewrite each function to be more comprehensive, so certain future tests blindsided the AI. Regardless, for both AI and man the tests and code were very good.

In part A, did the agent stick to the minimal implementation, and did it leave the tests alone?
- Minimal implementation only when I further increased restrictions on the Copilot instructions, so one had to be incredibly strict. I again had to forbid it from accessing the repository in full by prompting it in all cpas.

Did the agent at any point try to “cheat”, e.g. by hard-coding the value expected by the test?
- No. But I cannot test this 100% as I preempted this potential occurence by explicitly working it into the prompt, forbidding it from doing exactly that.

Which division of work, A or B, felt better, and why?
- I like doing things better with AI helping so neither really. I like the feeling of my own hands on code and keyboard. To me the code I write alone might not be as good but it is a matter of principle to keep my hands in control as I have had bad experiences with AI but acknolwedge the efficiency argument.