
type Operator = '+' | '-' | '*' | '/';

class Calculator {
    private currentInput: string = '';
    private previousInput: string = '';
    private operator: Operator | null = null;
    public appendNumber(number: string): void {
        if (this.currentInput === '0' && number !== '.') {
            this.currentInput = number;
        } else if (number === '.' && !this.currentInput.includes('.')) {
            this.currentInput += number;
        } else {
            this.currentInput += number;
        }
        this.updateDisplay();
    }
    public chooseOperator(operator: Operator): void {
        if (this.currentInput === '') return;
        if (this.previousInput !== '') {
            this.compute();
        }
        this.operator = operator;
        this.previousInput = this.currentInput;
        this.currentInput = '';
    }
    public compute(): void {
        let computation: number;
        const prev = parseFloat(this.previousInput);
        const current = parseFloat(this.currentInput);
        if (isNaN(prev) || isNaN(current)) return;
        switch (this.operator) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '/':
                computation = prev / current;
                break;
            default:
                return;
        }
        this.currentInput = computation.toString();
        this.operator = null;
        this.previousInput = '';
        this.updateDisplay();
    }
    public updateDisplay(): void {
        const display = document.getElementById('display') as HTMLInputElement;
        display.value = this.currentInput;
    }
    public clear(): void {
        this.currentInput = '';
        this.previousInput = '';
        this.operator = null;
        this.updateDisplay();
    }
}

const calculator = new Calculator();

document.getElementById('buttons')!.addEventListener('click', (event) => {
    const target = event.target as HTMLElement;
    if (target.classList.contains('number')) {
        calculator.appendNumber(target.innerText);
    } else if (target.classList.contains('operator')) {
        calculator.chooseOperator(target.innerText as Operator);
    } else if (target.classList.contains('equals')) {
        calculator.compute();
    } else if (target.classList.contains('clear')) {
        calculator.clear();
    }
});