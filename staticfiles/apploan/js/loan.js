    // JS to toggle REQ sections
document.querySelectorAll('.req-title').forEach(title => {
  title.addEventListener('click', () => {
    const body = title.nextElementSibling;
    const toggle = title.querySelector('.toggle');

    if (body.style.maxHeight) {
      // Faster close
      body.style.transition = 'max-height 0.15s ease, padding 0.15s ease, opacity 0.15s ease';
      body.style.maxHeight = null;
      body.style.opacity = 0;
      toggle.textContent = '+';
    } else {
      // Smooth open
      body.style.transition = 'max-height 1s ease, padding 0.35s ease, opacity 0.35s ease';
      body.style.maxHeight = body.scrollHeight + 'px';
      body.style.opacity = 1;
      toggle.textContent = '−';
    }
  });
});


document.addEventListener('DOMContentLoaded', function () {
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
});

function setupSlider(loanAmountId, interestRateId, monthsId, amountDisplayId, rateDisplayId, monthsDisplayId, repaymentId) {
  const loanAmount = document.getElementById(loanAmountId);
  const interestRate = document.getElementById(interestRateId);
  const loanMonths = document.getElementById(monthsId);

  const loanAmountDisplay = document.getElementById(amountDisplayId);
  const interestRateDisplay = document.getElementById(rateDisplayId);
  const loanMonthsDisplay = document.getElementById(monthsDisplayId);

  const monthlyRepayment = document.getElementById(repaymentId);

  function calculateLoan() {
    let P = parseFloat(loanAmount.value);
    let r = parseFloat(interestRate.value)/100/12;
    let n = parseFloat(loanMonths.value);
    let M = r === 0 ? P/n : (P*r*Math.pow(1+r,n))/(Math.pow(1+r,n)-1);
    monthlyRepayment.innerText = "$" + M.toFixed(2);
  }

  loanAmount.addEventListener("input", () => {
    loanAmountDisplay.innerText = loanAmount.value;
    calculateLoan();
  });
  interestRate.addEventListener("input", () => {
    interestRateDisplay.innerText = interestRate.value;
    calculateLoan();
  });
  loanMonths.addEventListener("input", () => {
    loanMonthsDisplay.innerText = loanMonths.value;
    calculateLoan();
  });

  calculateLoan(); // initial calculation
}

// Initialize both calculators
setupSlider(
  "carLoanAmount", "carInterestRate", "carLoanMonths",
  "carLoanAmountDisplay", "carInterestRateDisplay", "carLoanMonthsDisplay",
  "carMonthlyRepayment"
);

setupSlider(
  "motoLoanAmount", "motoInterestRate", "motoLoanMonths",
  "motoLoanAmountDisplay", "motoInterestRateDisplay", "motoLoanMonthsDisplay",
  "motoMonthlyRepayment"
);

document.querySelectorAll(".btn-increment, .btn-decrement").forEach(button => {
  button.addEventListener("click", () => {
    const targetId = button.getAttribute("data-target");
    const input = document.getElementById(targetId);
    const step = parseFloat(input.step) || 1;
    let value = parseFloat(input.value);

    if (button.classList.contains("btn-increment")) {
      value += step;
    } else {
      value -= step;
    }

    // Clamp value within min/max
    value = Math.max(parseFloat(input.min), Math.min(parseFloat(input.max), value));
    input.value = value;

    // Trigger input event to update display and repayment
    input.dispatchEvent(new Event("input"));
  });
});
