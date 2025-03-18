from csstack import Stack
import random
import string

class InfixPostfix:

    def infix_to_postfix(self, infix):
        stack = Stack()
        postfix = []

        precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

        for token in infix:
            if token in "0123456789":
                postfix.append(token)
            elif token == "(":
                stack.push(token)
            elif token == ")":
                if stack.is_empty():
                    raise ValueError(f"Unbalanced parentheses in expression: {infix}")
                popped = stack.pop()
                while popped != "(":
                    postfix.append(popped)
                    if stack.is_empty():
                        raise ValueError(f"Unbalanced parentheses in expression: {infix}")
                    popped = stack.pop()
            else:  # Handle operators
                while (not stack.is_empty() and
                    stack._data[stack._top] != "(" and
                    (precedence[stack._data[stack._top]] > precedence[token] or
                        (precedence[stack._data[stack._top]] == precedence[token] and token != "^"))):
                    popped = stack.pop()
                    postfix.append(popped)
                stack.push(token)

        while not stack.is_empty():
            popped = stack.pop()
            if popped == "(":
                raise ValueError(f"Unbalanced parentheses in expression: {infix}")
            postfix.append(popped)
        
        return "".join(postfix)
    
    @staticmethod
    def generate_infix(category: str):
        """Generate infix expressions based on category."""
        operators = ['+', '-', '*', '/', '^']

        if category == "small":
            num_operators = random.randint(1, 5)  # Reduced range for more manageable expressions
            use_parens = random.choice([True, False])

            expression = str(random.randint(0, 9))
            
            # Keep track of open parentheses
            open_parens = 0

            for _ in range(num_operators):
                operator = random.choice(operators)
                operand = str(random.randint(0, 9))

                if use_parens and random.random() < 0.3:
                    if random.random() < 0.5:
                        expression = f"({expression}){operator}{operand}"
                    else:
                        expression = f"{expression}{operator}({operand})"
                        open_parens += 1
                else:
                    expression = f"{expression}{operator}{operand}"
            
            # Close any remaining open parentheses
            expression += ")" * open_parens

            return expression
        
        elif category == "large":
            # Large Random test cases (more than 10 operators)
            num_operators = random.randint(10, 12)  # Further reduced for reliability
            expression = str(random.randint(0, 9))
            
            # Keep track of open parentheses
            open_parens = 0
            
            for _ in range(num_operators):
                operator = random.choice(operators)
                operand = str(random.randint(0, 9))
                
                # Add parentheses occasionally
                if random.random() < 0.2:
                    if random.random() < 0.5:
                        expression = f"({expression}){operator}{operand}"
                    else:
                        expression = f"{expression}{operator}({operand})"
                        open_parens += 1
                else:
                    expression = f"{expression}{operator}{operand}"
            
            # Close any remaining open parentheses
            expression += ")" * open_parens
            
            return expression
            
        elif category == "edge":
            edge_type = random.randint(1, 4)
            
            if edge_type == 1:
                # Maximum length (close to 40 chars)
                expression = str(random.randint(0, 9))
                while len(expression) < 37:  # Leave room for a few extra chars
                    operator = random.choice(operators)
                    operand = str(random.randint(0, 9))
                    expression = f"{expression}{operator}{operand}"
                return expression
                
            elif edge_type == 2:
                # Single operand
                return str(random.randint(0, 9))
                
            elif edge_type == 3:
                # Single operation
                return f"{random.randint(0, 9)}{random.choice(operators)}{random.randint(0, 9)}"
                
            else:
                # Alternating operators with same precedence
                expression = str(random.randint(0, 9))
                if random.random() < 0.5:
                    # Use + and -
                    ops = ['+', '-']
                    for i in range(random.randint(5, 10)):
                        expression += f"{random.choice(ops)}{random.randint(0, 9)}"
                else:
                    # Use * and /
                    ops = ['*', '/']
                    for i in range(random.randint(5, 10)):
                        expression += f"{random.choice(ops)}{random.randint(0, 9)}"
                return expression
                
        elif category == "weird":
            weird_type = random.randint(1, 4)
            
            if weird_type == 1:
                # Double parentheses
                expression = str(random.randint(0, 9))
                for _ in range(random.randint(3, 5)):
                    operator = random.choice(operators)
                    operand = str(random.randint(0, 9))
                    # Add double parentheses
                    expression = f"(({expression})){operator}{operand}"
                return expression
                
            elif weird_type == 2:
                # Chain of exponentiation
                expression = str(random.randint(1, 9))
                for _ in range(random.randint(3, 5)):
                    expression = f"{expression}^{random.randint(1, 5)}"
                return expression
                
            elif weird_type == 3:
                # Nested but balanced parentheses
                expression = str(random.randint(0, 9))
                for _ in range(random.randint(3, 5)):
                    expression = f"({expression})"
                    operator = random.choice(operators)
                    operand = str(random.randint(0, 9))
                    expression = f"{expression}{operator}{operand}"
                return expression
                
            else:
                # Mixed precedence operators
                expression = str(random.randint(0, 9))
                for _ in range(random.randint(5, 8)):
                    expression += random.choice(operators) + str(random.randint(0, 9))
                return expression
        else:
            return "1+1"  # Default case

    def generate_multiple_expressions(self, category, count=5):
        """Generate multiple expressions for a category"""
        expressions = []
        attempts = 0
        max_attempts = 50  # Limit the number of attempts to prevent infinite loops
        
        while len(expressions) < count and attempts < max_attempts:
            attempts += 1
            try:
                infix = InfixPostfix.generate_infix(category)
                # Validate expression by converting to postfix
                self.infix_to_postfix(infix)
                # Ensure we don't have duplicates
                if infix not in expressions:
                    expressions.append(infix)
            except Exception:
                # If there's an error, we just continue to the next attempt
                continue
                
        # If we couldn't generate enough expressions, use simpler fallbacks
        while len(expressions) < count:
            # Add simple valid expressions as fallbacks
            fallbacks = [
                f"{random.randint(1,9)}+{random.randint(1,9)}",
                f"{random.randint(1,9)}*{random.randint(1,9)}",
                f"({random.randint(1,9)}+{random.randint(1,9)})*{random.randint(1,9)}",
                f"{random.randint(1,9)}+{random.randint(1,9)}*{random.randint(1,9)}",
                f"{random.randint(1,9)}^{random.randint(1,9)}"
            ]
            for fallback in fallbacks:
                if len(expressions) < count and fallback not in expressions:
                    try:
                        # Validate fallback
                        self.infix_to_postfix(fallback)
                        expressions.append(fallback)
                    except:
                        continue
                        
        return expressions

    def write_test_file(self, filename="test_cases.txt"):
        """Write all test cases to a file."""
        with open(filename, "w") as f:
            # Write header
            f.write("# Test cases for Infix to Postfix conversion\n\n")
            
            # Large Random test cases
            f.write("# Large Random Test Cases (>10 operators)\n")
            large_cases = self.generate_multiple_expressions("large", 50)
            for infix in large_cases:
                try:
                    postfix = self.infix_to_postfix(infix)
                    f.write(f"{infix}    {postfix}\n")
                except Exception as e:
                    print(f"Skipping invalid expression: {infix} - {str(e)}")
            f.write("\n")
            
            # Small Real-World test cases
            f.write("# Small Real-World Test Cases (<10 operators)\n")
            small_cases = self.generate_multiple_expressions("small", 50)
            for infix in small_cases:
                try:
                    postfix = self.infix_to_postfix(infix)
                    f.write(f"{infix}    {postfix}\n")
                except Exception as e:
                    print(f"Skipping invalid expression: {infix} - {str(e)}")
            f.write("\n")
            
            # Edge test cases
            f.write("# Edge Test Cases\n")
            edge_cases = self.generate_multiple_expressions("edge", 50)
            for infix in edge_cases:
                try:
                    postfix = self.infix_to_postfix(infix)
                    f.write(f"{infix}    {postfix}\n")
                except Exception as e:
                    print(f"Skipping invalid expression: {infix} - {str(e)}")
            f.write("\n")
            
            # Weird test cases
            f.write("# Weird Test Cases\n")
            weird_cases = self.generate_multiple_expressions("weird", 50)
            for infix in weird_cases:
                try:
                    postfix = self.infix_to_postfix(infix)
                    f.write(f"{infix}    {postfix}\n")
                except Exception as e:
                    print(f"Skipping invalid expression: {infix} - {str(e)}")
            
            # Count actual written cases
            actual_case_count = 0
            with open(filename, 'r') as f_check:
                for line in f_check:
                    if not line.startswith('#') and line.strip():
                        actual_case_count += 1
                        
            print(f"Successfully wrote {actual_case_count} test cases to {filename}")
            
            # If we don't have enough cases, add simple ones to reach 20
            if actual_case_count < 20:
                with open(filename, 'a') as f_append:
                    f_append.write("\n# Additional Simple Test Cases\n")
                    simple_expressions = [
                        "1+2", "3*4", "5/6", "7-8", "9^2",
                        "1+2*3", "(1+2)*3", "4^2+5", "6*(7-8)", "9/(1+2)"
                    ]
                    
                    for i in range(min(20 - actual_case_count, len(simple_expressions))):
                        infix = simple_expressions[i]
                        postfix = self.infix_to_postfix(infix)
                        f_append.write(f"{infix}    {postfix}\n")
                    
                    print(f"Added {min(20 - actual_case_count, len(simple_expressions))} additional test cases to reach the required count.")

    @staticmethod
    def test_infix_to_postfix(infix):
        obj = InfixPostfix()
        try:
            result = obj.infix_to_postfix(infix)
            print(f"Infix: {infix} -> Postfix: {result}")
            return result
        except Exception as e:
            print(f"Error processing '{infix}': {str(e)}")
            return None
    
if __name__ == "__main__":
    
    print("\nGenerating test cases file...")
    generator = InfixPostfix()
    generator.write_test_file()