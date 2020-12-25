function getCreditHistoryValue() {
  var uiCred = document.getElementsByName("uiCred");
  for (var i in uiCred) {
    if (uiCred[i].checked) {
      return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function getRelationshipValue() {
  var uiRel = document.getElementsByName("uiRel");
  for (var i in uiRel) {
    if (uiRel[i].checked) {
      return parseInt(i);
    }
  }
  return -1; // Invalid Value
}
function getDependentsValue() {
  var uiDep = document.getElementsByName("uiDep");
  for (var i in uiDep) {
    if (uiDep[i].checked) {
      return parseInt(i);
    }
  }
  return -1; // Invalid Value
}
function getProperty_AreaValue() {
  var uiPropArea = document.getElementsByName("uiPropArea");
  for (var i in uiPropArea) {
    if (uiPropArea[i].checked) {
      return parseInt(i);
    }
  }
  return -1; // Invalid Value
}

function onClickedPredictStatus() {
  var loanAmt = document.getElementById("uiLoanAmt");
  var appInc = document.getElementById("uiAppInc");
  var coAppInc = document.getElementById("uiCoAppInc");
  var loanamttrm = document.getElementById("uiLoanAmtTrm");
  var cred = getCreditHistoryValue();
  var rel = getRelationshipValue();
  var dep = getDependentsValue();
  var prop = getProperty_AreaValue();
  var predStatus = document.getElementById("uiloanAppStatus");
  var url = "/predict_loanapp_status"; 

  $.post(
    url,
    {
      loan_amount: parseFloat(loanAmt.value),
      app_income: parseFloat(appInc.value),
      co_app_income: parseFloat(coAppInc.value),
      loan_amount_term: parseFloat(loanamttrm.value),
      cred: cred,
      rel:rel,
      dep:dep,
      prop:prop,
    },
    function (data, status) {
      console.log(data.loanStatus);
      predStatus.innerHTML =
        "<h2>" + data.loanStatus + "</h2>";
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
}

window.onload = onPageLoad;
