// ==============================
// TOGGLE REQ SECTIONS
// ==============================
document.querySelectorAll('.req-title').forEach(title => {
  title.addEventListener('click', () => {
    const body = title.nextElementSibling;
    const toggle = title.querySelector('.toggle');

    if (body.style.maxHeight) {
      body.style.maxHeight = null;
      body.style.opacity = 0;
      toggle.textContent = '+';
    } else {
      body.style.maxHeight = body.scrollHeight + 'px';
      body.style.opacity = 1;
      toggle.textContent = '−';
    }
  });
});

// ==============================
// TOOLTIP INIT
// ==============================
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => {
    new bootstrap.Tooltip(el);
  });
});

// ==============================
// LOAN CALCULATOR
// ==============================
function setupSlider(
  loanAmountId,
  interestRateId,
  termId,
  amountDisplayId,
  rateDisplayId,
  termDisplayId,
  repaymentId,
  isFlatRate,
  isMonthsSlider // Car uses months
) {
  const loanAmount = document.getElementById(loanAmountId);
  const interestRate = document.getElementById(interestRateId);
  const loanTerm = document.getElementById(termId);

  const loanAmountDisplay = document.getElementById(amountDisplayId);
  const interestRateDisplay = document.getElementById(rateDisplayId);
  const termDisplay = document.getElementById(termDisplayId);
  const monthlyRepayment = document.getElementById(repaymentId);

  function calculateLoan() {
    const P = Number(loanAmount.value);          // Principal
    const annualRate = Number(interestRate.value) / 100;
    const term = Number(loanTerm.value);         // Slider value
    const months = isMonthsSlider ? term : term * 12;

    let monthly;

    if (isFlatRate) {
      // Motorcycle: FLAT RATE (do not touch)
      const years = months / 12;
      const totalInterest = P * annualRate * years;
      monthly = (P + totalInterest) / months;
    } else {
      // Car: REDUCING BALANCE
      const r = annualRate / 12; // monthly interest rate
      monthly = r === 0
        ? P / months
        : (P * r * Math.pow(1 + r, months)) /
          (Math.pow(1 + r, months) - 1);
    }

    // Display values
    loanAmountDisplay.innerText = P.toLocaleString();
    interestRateDisplay.innerText = Number(interestRate.value).toFixed(2);
    termDisplay.innerText = term;
    monthlyRepayment.innerText = "$" + monthly.toFixed(2);
  }

  loanAmount.addEventListener("input", calculateLoan);
  interestRate.addEventListener("input", calculateLoan);
  loanTerm.addEventListener("input", calculateLoan);

  calculateLoan();
}

// ==============================
// INITIALISE
// ==============================
setupSlider(
  "carLoanAmount",
  "carInterestRate",
  "carLoanMonths",
  "carLoanAmountDisplay",
  "carInterestRateDisplay",
  "carLoanMonthsDisplay",
  "carMonthlyRepayment",
  false,   // reducing balance
  true     // Car slider is months
);

setupSlider(
  "motoLoanAmount",
  "motoInterestRate",
  "motoLoanMonths",
  "motoLoanAmountDisplay",
  "motoInterestRateDisplay",
  "motoLoanMonthsDisplay",
  "motoMonthlyRepayment",
  true,    // flat rate
  false    // Motorcycle slider is years
);

// ==============================
// + / − BUTTONS
// ==============================
document.querySelectorAll(".btn-increment, .btn-decrement").forEach(button => {
  button.addEventListener("click", () => {
    const input = document.getElementById(button.dataset.target);

    const min = Number(input.min);
    const max = Number(input.max);
    const step = Number(input.step) || 1;

    let value = Number(input.value);
    value += button.classList.contains("btn-increment") ? step : -step;
    value = Math.max(min, Math.min(max, value));

    input.value = value;

    // Force recalculation
    input.dispatchEvent(new Event("input", { bubbles: true }));
  });
});
